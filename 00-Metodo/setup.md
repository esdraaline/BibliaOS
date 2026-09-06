---
tipo: 
nome: Setup do ambiente
aliases: [setup, configuracao]
status: vazio
fontes: []
lacunas: []
termos_originais: []
tags: []
ultima_revisao: null
---

# Setup do Ambiente — BíbliaOS

> Documentação técnica do ambiente de trabalho do vault BíbliaOS.
> Não contém estudo bíblico — descreve a infraestrutura, configurações e procedimentos de reconstrução.
> Ref: PRD §5.1, §5.4, §9, §11, Apêndice B.

---

## 1. Princípios da Stack e Sobrevivência

1. **O app é descartável; os arquivos não.** O vault é composto exclusivamente por arquivos de texto puro em Markdown (`.md`) com frontmatter padronizado em YAML e links wiki (`[[link]]`). Se o Obsidian deixar de existir, o conhecimento acumulado permanece acessível em qualquer editor de texto.
2. **Zero plugins de terceiros no núcleo (D-02).** Toda a infraestrutura funcional do núcleo opera unicamente com os recursos nativos (*core*) do Obsidian: *Bases*, *Templates*, busca, backlinks e grafo. Nenhum plugin comunitário de terceiro é colocado no caminho crítico.
3. **Git exclusivo no desktop (D-04).** Versionamento e backup fora do dispositivo são operados pelo Git no computador principal, conectado a um repositório remoto privado no GitHub.
4. **Isolamento de configuração (D-05).** A pasta `.obsidian/` é totalmente ignorada pelo Git para evitar vazamento de credenciais, poluição de binários e churn de layout entre máquinas.

---

## 2. Plugins Nativos (Core) e Configurações

Ao abrir o vault no Obsidian pela primeira vez em uma máquina:

1. Acesse **Configurações** (`Settings` ou `Ctrl + ,`).
2. Em **Core plugins** (Plugins nativos):
   - **Bases:** Ativar. Responsável por renderizar o painel de sinais vitais (`_painel.base`).
   - **Templates:** Ativar. Responsável pela inserção de modelos com DNA padronizado.
   - **Backlinks:** Ativar (padrão).
   - **Page previews:** Ativar (padrão).
   - **Quick switcher:** Ativar (padrão).
   - **Search:** Ativar (padrão).
3. Na seção de opções de **Templates** (no menu lateral esquerdo de Configurações):
   - **Template folder location:** Definir como `_templates`.
4. Em **Community plugins** (Plugins da comunidade):
   - Manter **Restricted mode** como **ON** (modo restrito ativado, nenhum plugin de comunidade instalado/habilitado).

---

## 3. Versionamento Git e Backup

### Arquivos de Controle
- `.gitignore`: Protege `.obsidian/`, `.trash/` e `.DS_Store` contra rastreamento acidental.
- `.gitattributes`: Força normalização de quebras de linha (`* text=auto eol=lf`), impedindo que o Windows converta linhas para CRLF.

### Ritual Operacional
- **Ao iniciar a sessão de estudo:**
  ```bash
  git pull
  ```
- **Ao encerrar a sessão de estudo:**
  ```bash
  git add -A
  git commit -m "estudo: <resumo das notas criadas ou atualizadas>"
  git push
  ```

---

## 4. Captura Móvel (Fora do Vault)

Para registrar insights, leituras ou referências enquanto estiver longe do desktop:

1. **Não sincronizar o vault no celular (D-04).** O celular não possui cópia do vault, evitando riscos de segurança e conflitos de merge.
2. **App de escrita rápida:** Utilize um aplicativo externo leve já em uso (ex.: Google Keep com nota dedicada `"Inbox BibliaOS"`).
3. **Triagem semanal:** Durante a sessão semanal de revisão (~1h), abra a captura móvel no computador e transcreva os itens para a pasta `_inbox/` ou processe-os diretamente no vault, esvaziando a nota móvel.

---

## 5. Procedimento de Reconstrução do Zero (Nova Máquina)

Se você trocar de computador ou precisar recriar o ambiente a partir do repositório remoto:

1. **Clonar o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO_PRIVADO> bibliaos
   cd bibliaos
   ```
2. **Instalar o Obsidian:** Baixe e instale a versão oficial estável (ex.: 1.12.7 ou superior) em [obsidian.md](https://obsidian.md).
3. **Abrir a pasta como Vault:**
   - No Obsidian, selecione **Open folder as vault** e aponte para o diretório clonado (`bibliaos`).
4. **Configurar plugins nativos:**
   - Ative *Bases* e *Templates*.
   - Configure a pasta de modelos para `_templates`.
5. **Validar a integridade estrutural:**
   - Execute o verificador automatizado no terminal:
     ```bash
     python _projeto/verificar.py
     ```
   - O script deve retornar código `0` e aprovar todos os 12 checks.
6. **Validar o painel:**
   - Abra o arquivo `_painel.base` e confirme a visualização das 6 views.

---

## 6. Procedimento de Contingência (Obsidian Descontinuado)

Se o aplicativo Obsidian for descontinuado ou se você optar por migrar:

1. Todos os arquivos de notas estão armazenados em texto puro Markdown (`.md`) organizados nas pastas numeradas (`00-` a `09-`).
2. O corpus pode ser aberto diretamente no **VS Code**, Neovim, Logseq, ou qualquer editor de texto com suporte a Markdown.
3. A integridade estrutural continua sendo auditada independentemente de qualquer editor rodando:
   ```bash
   python _projeto/verificar.py
   ```
4. As regras de links wiki (`[[Nome da Nota]]`) são compatíveis com a maioria das ferramentas de gestão de conhecimento pessoal (PKM).

---

## 7. Rituais e Cadência (PRD §11)

| Ritmo | Duração | Ações | Limites e Tetos |
|---|---|---|---|
| **Diário** | 20–30 min | Executar **uma** das três ações:<br>1. Avançar 1 eixo do dossiê aberto<br>2. Avançar ou revisar 1 nota da fila<br>3. Capturar insights | Máximo 1 nota nova entrando no pipeline por dia. |
| **Semanal** | ~1h | 1. Esvaziar `_inbox/`<br>2. Revisar a view *Pipeline* no `_painel.base`<br>3. Conferir os tetos de WIP | Máximo 3 notas em `pesquisando`.<br>Máximo 5 notas em `rascunho`/`em-revisao`.<br>Máximo 1 dossiê aberto. |
| **Trimestral** | 1–2h | 1. Regeneração periódica (revisar 2–3 notas `consolidado` com `ultima_revisao` mais antiga)<br>2. Priorizar camadas opcionais de dossiês fechados<br>3. Varrer a pauta de lacunas | Atualizar a propriedade `ultima_revisao` das notas revisadas com a data da revisão. |
