# Log de decisões

Uma linha por decisão que **não** era óbvia. Existe para impedir que uma escolha já debatida volte disfarçada de melhoria três meses depois.

**Formato:** `D-NN | data | decisão | alternativa descartada | motivo | estado`

Estados: **fechada** (não reabrir sem argumento novo) · **aberta** (ainda decidindo) · **revista** (mudou; a antiga fica no histórico)

---

## Decisões fechadas — vêm do PRD, não reabrir

| # | Decisão | Alternativa descartada | Motivo | Estado |
|---|---|---|---|---|
| D-01 | Obsidian como app | VS Code puro, Logseq, Notion | Não pelo recurso, pela saída: markdown puro no disco. O app é descartável, o corpus não | fechada |
| D-02 | Zero plugins de terceiro no núcleo | Kanban, Dataview, Smart Connections, Templater | Sistema para durar 20 anos não põe projeto de fim de semana de mantenedor único no caminho crítico | fechada |
| D-03 | Bases (core) para painel e board | Plugin Kanban + Status Updater | O board seria a peça mais frágil da stack para economizar cliques num pipeline de 8 itens | fechada |
| D-04 | Git só no desktop; captura móvel fora do vault | Plugin de sync mobile via API do GitHub | PAT em texto puro dentro do vault, plugin jovem, conflito de merge resolvido na tela do celular | fechada |
| D-05 | `.obsidian/` inteiro no `.gitignore` | Ignorar só `workspace.json` | Evita commitar segredo de plugin, binário e churn de layout de uma vez | fechada |
| D-06 | `.gitattributes` com `eol=lf` | Deixar o padrão do Windows | Sem isso cada arquivo tocado vira diff de arquivo inteiro e o histórico fica ilegível | fechada |
| D-07 | Nomes de arquivo com acento + `aliases` | Nomes ASCII sem acento | `[[Gênesis]]` não resolve contra `Genesis.md`; `Jó`/`João` colidem sem acento | fechada |
| D-08 | Sem `relacionados`, sem `status_desde`, sem detector de estagnação | Campos declarados à mão e query por data | Campo de auditoria mantido à mão apodrece; `file.mtime` não sobrevive ao Git; e o teto de WIP já resolvia | fechada |
| D-09 | 10 pastas, `tipo` como classificador | 16 pastas temáticas | Cada pasta é uma decisão cobrada em toda criação de nota — atrito no ritual diário, que é onde o projeto morre | fechada |
| D-10 | Dossiê de palavra ancorado no termo original; português vira `tipo: porta` | Uma ficha por palavra em português | "Amor" em português recorta uma decisão de tradutor, não um termo bíblico | fechada |
| D-11 | Sem barra de progresso de dossiê | Campo `eixos_fechados` + view | Campo à mão para vigiar um objeto já limitado a um. Limite bem posto dispensa sensor | fechada |
| D-12 | `_projeto/` entra no filtro global do painel, junto com `_templates` e `_inbox` | Repositório separado do vault | Mantém uma pasta só para VS Code e Obsidian; o filtro impede que o PRD apareça como nota de estudo | fechada |
| D-13 | O vault é a **fonte**; site, PDF e cofre são saídas geradas (PRD §14) | Tratar o vault como produto final | Markdown com frontmatter é banco de dados: uma fonte, várias saídas, nenhuma escrita à mão | fechada |
| D-14 | Site com Quartz, **privado por padrão**, gatilho ~50 notas `consolidado` | Obsidian Publish (pago); publicar desde o início | Quartz lê o vault como está e é dependência de derivação, não de núcleo. Site nasce privado porque o que é indexado não se despublica | fechada |
| D-15 | Publicação filtra por `status: consolidado` menos tag `privado` | Campo novo `publicar: true` | Campo novo seria manutenção manual contra §5.3 e D-08; `consolidado` já significa "passou pelo critério de fechamento" | fechada |
| D-16 | Export em PDF é **por dossiê**, nunca do vault inteiro; Drive é cofre, não sistema | "Um grande livro" do corpus; Drive como fundação | Livro do corpus é fotografia de organismo vivo. Drive não tem backlink nem busca em markdown — como destino de zip trimestral, é ótimo | fechada |

---

## Decisões novas

Acrescente abaixo. O agente registra aqui toda escolha que fizer e que o PRD não determinava.

| # | Data | Decisão | Alternativa descartada | Motivo | Estado |
|---|---|---|---|---|---|
| D-17 | 2026-08-04 | Corrigir duas inconsistências textuais herdadas da promoção do PRD de v10 para v11: `CLAUDE.md` dizia "Cinco decisões já fechadas" listando seis, e `CLAUDE.md`/`S0-abertura.md` ainda referenciavam "PRD.md (v10)" | Deixar como estava, ou corrigir mais linhas além das apontadas | O PRD real em disco é v11; as referências desatualizadas confundiriam sessões futuras sobre qual é a lei vigente | fechada |
| D-19 | 2026-09-06 | Sintaxe do `.base` reconciliada contra o Obsidian 1.13.7 rodando de verdade, com conferência por captura de tela: colunas exibidas são `order:` (não `columns:`, que o app ignora em silêncio), `direction` de `sort`/`groupBy` é MAIÚSCULO (`ASC`/`DESC` — em minúsculo o app apaga a chave ao salvar), e o filtro global ganhou `file.ext == "md"` e `file.hasProperty("status")` | Manter a sintaxe entregue no S2, que renderizava sem erro visível mas mentia; ou pedir ao Josemar que montasse as views pela interface | O Bases indexa todo arquivo do vault, não só `.md`: sem os dois filtros novos, a view Pipeline listava `gerar_fichas.py`, `CLAUDE.md`, `setup.md` e o próprio `_painel.base` — arquivos sem `status`, que passavam no teste `status != "vazio"` por serem nulos. O painel mentia desde o primeiro dia, exatamente o que PRD §9 quer evitar | fechada |
| D-18 | 2026-09-06 | `_projeto/verificar.py` exclui `_templates/` inteira e `00-Metodo/setup.md` da varredura de notas (checks 3–12); os checks 4 e 5 voltaram a exigir `tipo` e `status` sempre presentes e válidos, sem exceção | Deixar `tipo`/`status` vazio passar batido em qualquer nota (versão inicial entregue pelo Antigravity no S2); ou criar um 14º valor de `tipo` só para documentação técnica | `_templates/nota.md` tem `tipo` em branco de propósito (é template genérico, e o `_painel.base` já exclui `_templates/` do filtro por essa razão) e `00-Metodo/setup.md` é documentação do ambiente, não nota de estudo (CLAUDE.md já trata os dois como categoria à parte). Excluir os dois da varredura resolve a causa raiz sem abrir exceção nos checks nem mexer no enum do PRD §5.3 | fechada |
| D-20 | 2026-09-06 | Caminho C para notas estruturais/método: as 4 notas de método mantêm frontmatter completo e sujeição aos 12 checks, com exceção pontual explícita apenas no check_04 (sem campo `tipo`); `indice-de-povos.md` é tabela pura excluída de `get_all_notes()` como `setup.md` | Caminho A (excluir as 5 do `verificar.py`, desativando checks 10–12 nelas) e Caminho B (forçar um `tipo` do enum como `tema`/`povo`, poluindo filtros futuros) | As 4 notas de método passarão pelo ciclo de vida de estudo (`vazio` → `consolidado`) e necessitam da proteção dos checks 10–12 para barrar consolidação sem fonte ou sem links; já o índice de povos é tabela estrutural pura sem afirmações ou ciclo de consolidação | fechada |
