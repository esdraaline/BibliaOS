# STATUS

> Este arquivo é a memória do projeto entre sessões. O agente o atualiza ao fim de cada sprint.
> Se você voltar daqui a três semanas, leia só isto e saberá onde parou.

**Última atualização:** 2026-09-06
**Sprint atual:** S4 — Módulo dossiê
**Próximo prompt a colar:** `_projeto/prompts/S4-dossie.md`

---

## Estado atual

Repositório Git válido, branch `main`, com a estrutura de pastas do PRD §5.2 criada, 66 fichas de livros geradas em `02-Livros/`, 4 notas-mestras de método/contexto em `00-Metodo/` e `01-Contexto/`, 1 índice tabular `01-Contexto/indice-de-povos.md`, templates básicos em `_templates/`, script de geração idempotente na raiz, painel de controle `_painel.base`, manual técnico `00-Metodo/setup.md` e suíte de integridade `_projeto/verificar.py` com 12 checks automatizados aprovados.

**O que existe:**
- `CLAUDE.md`
- `_projeto/` com PRD v11, README, SPRINTS, DECISOES, STATUS e os prompts
- `.gitignore` e `.gitattributes` (conferidos contra PRD §5.4, sem alteração)
- Repositório Git inicializado, branch `main`, commits de S0, S1, S2 e S3
- As 12 pastas do PRD §5.2 (10 numeradas + `_templates/` + `_inbox/`)
- `gerar_fichas.py` na raiz
- 66 fichas de livros em `02-Livros/` (frontmatter YAML completo e cabeçalhos de estudo vazios)
- 4 notas estruturais de método/contexto (`00-Metodo/hermeneutica-e-exegese-basica.md`, `00-Metodo/falacias-de-estudo-de-palavra.md`, `00-Metodo/formacao-do-canon.md`, `01-Contexto/cronologia-biblica.md`) com frontmatter e cabeçalhos vazios
- 1 índice estrutural tabular `01-Contexto/indice-de-povos.md` (tabela com cabeçalho e zero linhas)
- `_templates/nota.md` e `_templates/prompts.md`
- `_painel.base` com as 6 views do PRD §9 e filtro global
- `00-Metodo/setup.md` com documentação técnica do ambiente
- `_projeto/verificar.py` com os 12 checks de integridade passando com código 0
- Remoto no GitHub conectado: `origin` → https://github.com/esdraaline/BibliaOS (privado)

**O que não existe ainda:**
- Templates especializados de dossiê (`dossie-palavra.md`, `dossie-tema.md`, `porta.md`) e conteúdo dos prompts (S4)
- Ficha de porta `08-Palavras/Amor.md` e fichas de termos mapeados (S4)
- Qualquer nota de estudo bíblico com conteúdo preenchido

---

## Progresso dos sprints

| Sprint | Estado | Data | Observação |
|---|---|---|---|
| S0 — Fundação do repositório | ✅ concluído | 2026-08-04 | Ver evidência no commit `sprint(S0)` |
| S1 — Esqueleto do vault | ✅ concluído | 2026-09-04 | 66 fichas em 02-Livros/, gerar_fichas.py, nota.md e prompts.md |
| S2 — Painel, setup e testes | ✅ concluído | 2026-09-06 | _painel.base (6 views), 00-Metodo/setup.md e _projeto/verificar.py (12 checks) |
| S3 — Esqueletos de método | ✅ concluído | 2026-09-06 | 5 arquivos em 00-Metodo e 01-Contexto; D-20 (Caminho C) com checks 10-12 ativos |
| S4 — Módulo dossiê | ⬜ pendente | — | — |
| S5 — Auditoria de nascimento | ⬜ pendente | — | — |

---

## Pendências do Josemar (não do agente)

- [x] Criar repositório **privado** no GitHub e conectar como remoto
- [x] Instalar o Obsidian e abrir esta pasta como vault — Obsidian 1.13.7, vault aberto em `C:\projetos\bibliaos`
- [x] Ativar os plugins core Bases e Templates — ambos ativos, pasta de modelos `_templates`; nenhum plugin de comunidade habilitado (`.obsidian/plugins` não existe)
- [x] Escolher o app de captura no celular (PRD §5.4) — Google Keep, nota "Inbox BibliaOS" criada, sem sync com o vault
- [x] Abrir `_painel.base` no Obsidian e confirmar renderização visual — feito em 2026-09-06 no Obsidian 1.13.7, com captura de tela: a view Pipeline renderiza sem erro, com as 4 colunas (`file.name`, `tipo`, `status`, `ultima_revisao`) e 0 resultado, que é o esperado enquanto todas as 66 fichas estão em `status: vazio`
- [ ] Preencher o conteúdo de `00-Metodo/` depois do S3

---

## Bloqueios

Nenhum.

---

## Últimas decisões registradas

Ver `_projeto/DECISOES.md`. As decisões D-01 a D-16 já estão fechadas e vêm do PRD — não devem ser reabertas pelo agente. D-17 (S0): correção de inconsistências textuais herdadas do PRD v10 → v11. D-18 (S2): `verificar.py` exclui `_templates/` e `00-Metodo/setup.md` da varredura de notas; checks 4 e 5 voltaram a exigir `tipo`/`status` sempre válidos, sem exceção. D-19 (S2): sintaxe do `.base` reconciliada contra o Obsidian 1.13.7 real (`order:` em vez de `columns:`, `direction` maiúsculo, filtro global com `file.ext` e `file.hasProperty`). D-20 (S3): Caminho C implementado — 4 notas de método mantêm frontmatter completo e proteção dos checks 10–12 com exceção explícita restrita a `check_04`; `indice-de-povos.md` como tabela pura fora de `get_all_notes()`.
