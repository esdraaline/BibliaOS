#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificação de integridade estrutural do vault BibliaOS.
Implementa os 12 checks obrigatórios definidos no Sprint S2 (PRD §5.2, §5.3, §5.4, §9 e SPRINTS.md).
Utiliza exclusivamente a biblioteca padrão do Python.
Retorna código de saída 0 se todos os checks passarem, ou 1 se houver falhas.
"""

from pathlib import Path
import re
import subprocess
import sys

# Diretórios e enums padronizados do PRD §5.2 e §5.3
PASTAS_PRD_5_2 = [
    "00-Metodo",
    "01-Contexto",
    "02-Livros",
    "03-Personagens",
    "04-Temas",
    "05-Doutrinas",
    "06-Passagens",
    "07-Apologetica",
    "08-Palavras",
    "09-Biblioteca",
    "_templates",
    "_inbox",
]

ENUM_TIPOS = {
    "livro",
    "personagem",
    "povo",
    "lugar",
    "periodo",
    "tema",
    "doutrina",
    "passagem",
    "apologetica",
    "filosofia",
    "palavra",
    "porta",
    "obra",
}

ENUM_STATUS = {
    "vazio",
    "pesquisando",
    "rascunho",
    "em-revisao",
    "consolidado",
}

PROPRIEDADES_PERMITIDAS = {
    "tipo",
    "nome",
    "aliases",
    "testamento",
    "secao",
    "status",
    "fontes",
    "lacunas",
    "termos_originais",
    "tags",
    "ultima_revisao",
}


def parse_frontmatter(content: str):
    """
    Parser robusto de frontmatter YAML usando apenas a biblioteca padrão.
    Retorna (propriedades: dict, corpo: str, erro: str | None).
    """
    if not content.startswith("---"):
        return None, None, "Arquivo não inicia com delimitador de frontmatter ('---')"

    # Separa o frontmatter do corpo
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", content, re.DOTALL)
    if not match:
        return None, None, "Frontmatter não delimitado corretamente por '---'"

    raw_fm = match.group(1)
    body = match.group(2)

    props = {}
    current_list_key = None

    for line in raw_fm.splitlines():
        # Ignora linhas vazias e comentários puros
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue

        # Item de lista multiline: '  - valor' ou '- valor'
        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_list_key:
            item_val = list_match.group(1).strip()
            # Remove aspas se existirem
            if (item_val.startswith('"') and item_val.endswith('"')) or (
                item_val.startswith("'") and item_val.endswith("'")
            ):
                item_val = item_val[1:-1]
            if not isinstance(props[current_list_key], list):
                props[current_list_key] = []
            props[current_list_key].append(item_val)
            continue

        # Linha chave: valor
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()

            # Remove comentários inline
            if "#" in val and not (val.startswith('"') or val.startswith("'")):
                val = val.split("#")[0].strip()

            # Lista inline: [a, b, c] ou []
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                if not inner:
                    props[key] = []
                else:
                    items = []
                    for it in inner.split(","):
                        it_clean = it.strip()
                        if (it_clean.startswith('"') and it_clean.endswith('"')) or (
                            it_clean.startswith("'") and it_clean.endswith("'")
                        ):
                            it_clean = it_clean[1:-1]
                        if it_clean:
                            items.append(it_clean)
                    props[key] = items
                current_list_key = None
            elif val == "" or val.lower() == "null" or val == "~":
                props[key] = None
                current_list_key = key  # Pode ser início de lista multiline
            else:
                if (val.startswith('"') and val.endswith('"')) or (
                    val.startswith("'") and val.endswith("'")
                ):
                    val = val[1:-1]
                props[key] = val
                current_list_key = None
        else:
            current_list_key = None

    return props, body, None


def get_all_notes(vault_root: Path):
    """
    Retorna lista de todas as notas de conteúdo do vault: fora de _projeto/,
    _templates/ (templates não são conteúdo — mesmo filtro do _painel.base) e
    de arquivos de controle como CLAUDE.md e 00-Metodo/setup.md (documentação
    técnica do ambiente, não nota de estudo).
    """
    notes = []
    for path in vault_root.rglob("*.md"):
        # Ignora arquivos em _projeto, _templates, .git, .obsidian, .trash
        rel = path.relative_to(vault_root)
        parts = rel.parts
        if (
            parts[0] == "_projeto"
            or parts[0] == "_templates"
            or parts[0].startswith(".")
            or parts[0] == ".trash"
            or path.name == "CLAUDE.md"
            or rel == Path("00-Metodo/setup.md")
        ):
            continue
        notes.append(path)
    return sorted(notes)


# ==============================================================================
# OS 12 CHECKS OBRIGATÓRIOS DO SPRINT S2
# ==============================================================================


def check_01_pastas_obrigatorias(vault_root: Path):
    """Check 1: As 12 pastas do PRD §5.2 existem."""
    faltando = []
    for pasta in PASTAS_PRD_5_2:
        dir_path = vault_root / pasta
        if not dir_path.is_dir():
            faltando.append(pasta)
    if faltando:
        return False, f"Pastas ausentes: {', '.join(faltando)}"
    return True, f"Todas as {len(PASTAS_PRD_5_2)} pastas obrigatórias existem"


def check_02_total_fichas_livros(vault_root: Path):
    """Check 2: Existem exatamente 66 fichas em 02-Livros/."""
    pasta_livros = vault_root / "02-Livros"
    if not pasta_livros.is_dir():
        return False, "Pasta 02-Livros/ não encontrada"
    fichas = list(pasta_livros.glob("*.md"))
    total = len(fichas)
    if total != 66:
        return False, f"Esperado 66 fichas, encontrado {total}"
    return True, f"Exatamente {total} fichas em 02-Livros/"


def check_03_frontmatter_valido(vault_root: Path):
    """Check 3: Todo .md fora de _projeto/ tem frontmatter YAML válido."""
    notes = get_all_notes(vault_root)
    erros = []
    for note in notes:
        try:
            content = note.read_text(encoding="utf-8")
        except Exception as e:
            erros.append(f"{note.relative_to(vault_root)}: erro ao ler ({e})")
            continue
        props, _, err = parse_frontmatter(content)
        if err:
            erros.append(f"{note.relative_to(vault_root)}: {err}")
    if erros:
        return False, f"Frontmatter inválido em {len(erros)} arquivo(s):\n  " + "\n  ".join(erros)
    return True, f"Frontmatter válido em todas as {len(notes)} notas analisadas"


def check_04_tipo_enum(vault_root: Path):
    """Check 4: Todo `tipo` está no enum de PRD §5.3 — nenhum valor inventado."""
    notes = get_all_notes(vault_root)
    invalidos = []
    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        val_tipo = props.get("tipo") if props else None
        if not val_tipo or not str(val_tipo).strip():
            invalidos.append(f"{note.relative_to(vault_root)}: tipo ausente ou vazio")
        elif str(val_tipo).strip() not in ENUM_TIPOS:
            invalidos.append(f"{note.relative_to(vault_root)}: tipo='{val_tipo}' inválido")
    if invalidos:
        return False, f"Tipos fora do enum em:\n  " + "\n  ".join(invalidos)
    return True, "Todos os campos `tipo` estão no enum do PRD §5.3"


def check_05_status_enum(vault_root: Path):
    """Check 5: Todo `status` está no enum de PRD §5.3."""
    notes = get_all_notes(vault_root)
    invalidos = []
    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        val_status = props.get("status") if props else None
        if not val_status or not str(val_status).strip():
            invalidos.append(f"{note.relative_to(vault_root)}: status ausente ou vazio")
        elif str(val_status).strip() not in ENUM_STATUS:
            invalidos.append(f"{note.relative_to(vault_root)}: status='{val_status}' inválido")
    if invalidos:
        return False, f"Status fora do enum em:\n  " + "\n  ".join(invalidos)
    return True, "Todos os campos `status` estão no enum do PRD §5.3"


def check_06_propriedades_permitidas(vault_root: Path):
    """Check 6: Nenhuma propriedade fora da lista de PRD §5.3 aparece em qualquer nota."""
    notes = get_all_notes(vault_root)
    invalidas = []
    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        if props:
            estranhas = set(props.keys()) - PROPRIEDADES_PERMITIDAS
            if estranhas:
                invalidas.append(f"{note.relative_to(vault_root)}: propriedades extras {list(estranhas)}")
    if invalidas:
        return False, f"Propriedades não permitidas encontradas:\n  " + "\n  ".join(invalidas)
    return True, "Nenhuma propriedade fora do DNA do PRD §5.3 foi encontrada"


def check_07_aliases_unicos(vault_root: Path):
    """Check 7: Nenhum alias aparece em duas notas diferentes."""
    notes = get_all_notes(vault_root)
    alias_map = {}
    duplicados = []

    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        if props and "aliases" in props:
            aliases = props["aliases"]
            if isinstance(aliases, list):
                for alias in aliases:
                    alias_str = str(alias).strip()
                    if not alias_str:
                        continue
                    if alias_str in alias_map:
                        duplicados.append(
                            f"Alias '{alias_str}' duplicado em '{alias_map[alias_str]}' e '{note.name}'"
                        )
                    else:
                        alias_map[alias_str] = note.name

    if duplicados:
        return False, f"Aliases duplicados encontrados:\n  " + "\n  ".join(duplicados)
    return True, f"Todos os {len(alias_map)} aliases declarados são estritamente únicos"


def check_08_sem_crlf(vault_root: Path):
    """Check 8: Nenhum arquivo contém CRLF."""
    arquivos_crlf = []
    for path in vault_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(vault_root)
        if rel.parts[0] in {".git", ".trash", ".obsidian"}:
            continue
        try:
            raw_bytes = path.read_bytes()
            if b"\r\n" in raw_bytes:
                arquivos_crlf.append(str(rel))
        except Exception:
            continue

    if arquivos_crlf:
        return False, f"Arquivos com quebra CRLF ({len(arquivos_crlf)}):\n  " + "\n  ".join(arquivos_crlf)
    return True, "Nenhum arquivo contém CRLF (todos utilizam LF exclusivamente)"


def check_09_obsidian_ignorado_git(vault_root: Path):
    """Check 9: .obsidian/ não está rastreado pelo Git."""
    # 1. Verifica se há arquivos rastreados em .obsidian
    try:
        res = subprocess.run(
            ["git", "ls-files", ".obsidian"],
            cwd=vault_root,
            capture_output=True,
            text=True,
            check=True,
        )
        rastreados = res.stdout.strip()
        if rastreados:
            return False, f"Arquivos dentro de .obsidian/ estão rastreados no Git:\n{rastreados}"
    except Exception as e:
        return False, f"Erro ao executar git ls-files: {e}"

    # 2. Confirma regra no .gitignore
    gitignore = vault_root / ".gitignore"
    if not gitignore.exists() or ".obsidian" not in gitignore.read_text(encoding="utf-8"):
        return False, ".obsidian não está presente no .gitignore"

    return True, ".obsidian/ não está rastreado e está protegido no .gitignore"


def check_10_consolidado_fontes_ou_lacunas(vault_root: Path):
    """Check 10: Nenhuma nota `consolidado` sem `fontes` e sem `lacunas`."""
    notes = get_all_notes(vault_root)
    erros = []
    total_consolidados = 0

    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        if props and props.get("status") == "consolidado":
            total_consolidados += 1
            fontes = props.get("fontes") or []
            lacunas = props.get("lacunas") or []
            tem_fontes = isinstance(fontes, list) and len([f for f in fontes if str(f).strip()]) > 0
            tem_lacunas = isinstance(lacunas, list) and len([l for l in lacunas if str(l).strip()]) > 0
            if not tem_fontes and not tem_lacunas:
                erros.append(
                    f"{note.relative_to(vault_root)}: nota consolidada sem fontes citadas e sem lacunas declaradas"
                )

    if erros:
        return False, f"Notas consolidadas sem fonte e sem lacuna ({len(erros)}):\n  " + "\n  ".join(erros)
    return True, f"Nenhuma nota consolidada sem fonte/lacuna ({total_consolidados} consolidadas no total)"


def check_11_consolidado_tem_link(vault_root: Path):
    """Check 11: Nenhuma nota `consolidado` sem ao menos um `[[link]]` no corpo."""
    notes = get_all_notes(vault_root)
    erros = []
    total_consolidados = 0

    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, body, _ = parse_frontmatter(content)
        if props and props.get("status") == "consolidado":
            total_consolidados += 1
            if not body or not re.search(r"\[\[.+?\]\]", body):
                erros.append(
                    f"{note.relative_to(vault_root)}: nota consolidada sem ao menos um [[link]] no corpo"
                )

    if erros:
        return False, f"Notas consolidadas sem links wiki ({len(erros)}):\n  " + "\n  ".join(erros)
    return True, f"Todas as notas consolidadas contêm [[links]] ({total_consolidados} consolidadas no total)"


def check_12_consolidado_ultima_revisao(vault_root: Path):
    """Check 12: Nenhuma nota `consolidado` com `ultima_revisao` nulo."""
    notes = get_all_notes(vault_root)
    erros = []
    total_consolidados = 0

    for note in notes:
        content = note.read_text(encoding="utf-8")
        props, _, _ = parse_frontmatter(content)
        if props and props.get("status") == "consolidado":
            total_consolidados += 1
            rev = props.get("ultima_revisao")
            if rev is None or not str(rev).strip() or str(rev).strip().lower() == "null":
                erros.append(
                    f"{note.relative_to(vault_root)}: nota consolidada com ultima_revisao nulo/ausente"
                )

    if erros:
        return False, f"Notas consolidadas com data de revisão nula ({len(erros)}):\n  " + "\n  ".join(erros)
    return True, f"Todas as notas consolidadas possuem ultima_revisao preenchida ({total_consolidados} consolidadas no total)"


CHECKS = [
    ("Check 01: Pastas obrigatórias do PRD §5.2", check_01_pastas_obrigatorias),
    ("Check 02: Total de 66 fichas em 02-Livros/", check_02_total_fichas_livros),
    ("Check 03: Frontmatter YAML válido em todas as notas", check_03_frontmatter_valido),
    ("Check 04: Enum de tipos conforme PRD §5.3", check_04_tipo_enum),
    ("Check 05: Enum de status conforme PRD §5.3", check_05_status_enum),
    ("Check 06: Propriedades permitidas (DNA) do PRD §5.3", check_06_propriedades_permitidas),
    ("Check 07: Unicidade global de aliases", check_07_aliases_unicos),
    ("Check 08: Ausência de quebras CRLF", check_08_sem_crlf),
    ("Check 09: .obsidian/ protegido fora do Git", check_09_obsidian_ignorado_git),
    ("Check 10: Notas consolidadas possuem fontes ou lacunas", check_10_consolidado_fontes_ou_lacunas),
    ("Check 11: Notas consolidadas possuem ao menos um [[link]]", check_11_consolidado_tem_link),
    ("Check 12: Notas consolidadas possuem ultima_revisao", check_12_consolidado_ultima_revisao),
]


def main():
    vault_root = Path(__file__).resolve().parent.parent
    print("=" * 70)
    print(" BíbliaOS — Verificação de Integridade Estrutural")
    print(f" Raiz do vault: {vault_root}")
    print("=" * 70)

    sucessos = 0
    falhas = 0

    for nome, func in CHECKS:
        ok, msg = func(vault_root)
        if ok:
            sucessos += 1
            print(f"[OK]   {nome} -> {msg}")
        else:
            falhas += 1
            print(f"[FALHA] {nome} -> {msg}")

    print("=" * 70)
    if falhas == 0:
        print(f"Resultado: SUCESSO. Todos os {sucessos} checks passaram.")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"Resultado: FALHA. {falhas} falha(s) encontrada(s), {sucessos} check(s) aprovado(s).")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()
