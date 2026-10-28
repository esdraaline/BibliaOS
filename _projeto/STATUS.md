# STATUS

> Este arquivo é a memória do projeto entre sessões. O agente o atualiza ao fim de cada sprint.
> Se você voltar daqui a três semanas, leia só isto e saberá onde parou.

**Última atualização:** 2026-10-28
**Fase atual:** Redesenho do produto solicitado pelo Josemar. O PRD v11 descreve a implementação anterior em Obsidian; ainda não descreve a plataforma desejada.
**Construção:** Sprints S0 a S5 concluídos

---

## Direção atual, definida em 26/10/2026

Josemar quer que o BíbliaOS seja **sua própria plataforma**, com leitura bíblica, anotações e pesquisa na mesma interface, tanto quanto possível. Um link para uma Bíblia online pode complementar a experiência, mas não deve obrigá-lo a alternar entre aplicativos como fluxo principal. A recomendação anterior de usar YouVersion, Google Keep, Obsidian e STEP Bible em sequência foi rejeitada. O Logos também foi rejeitado como substituto, pois o objetivo é criar o BíbliaOS.

**MVP proposto para validar essa direção:** uma tela de estudo responsiva centrada na referência bíblica (livro, capítulo e versículo), com (1) acesso a várias versões, (2) nota ligada à passagem selecionada, (3) busca nas próprias notas e nas fontes disponíveis, e (4) área de pesquisa. A RC69 é a versão portuguesa preferida do Josemar. O estudo do Antigo Testamento deve oferecer acesso ao texto hebraico e, nos trechos correspondentes, aramaico; o Novo Testamento deve oferecer acesso ao grego. O primeiro teste real deve ser: abrir Gênesis 1, acessar RC69 e hebraico a partir do BíbliaOS, registrar uma nota sobre a passagem e reencontrá-la. Sincronização entre máquinas e celular deve ser prevista desde o desenho; ainda não foi implementada.

**Fonte do texto bíblico:** distinguir links para leitura no site autorizado da exibição do texto dentro do BíbliaOS. A RC69 é uma edição da SBB protegida por direitos; a Bíblia Online a mostra com autorização. O BíbliaOS pode oferecer link direto por referência, mas incorporar ou reproduzir o texto completo requer uma fonte com autorização aplicável. Um teste de 26/10/2026 encontrou `X-Frame-Options: SAMEORIGIN` na Bíblia Online, então não planejar seu site em iframe. Para hebraico, Tanach.us permite copiar seu texto bíblico, respeitando a identificação da edição; Sefaria e STEP Bible são opções de links. A escolha técnica e as licenças de cada fonte ainda serão validadas na implementação.

**Estado:** direção registrada; aplicativo, migração de notas e novo PRD ainda não implementados. O guia publicado no GitHub Pages documenta a implementação anterior.

**Protótipo NotebookLM/Gemini Notebook (26/10/2026):** criado na conta `lojadares` o caderno privado [BíbliaOS | Criação](https://notebook.google.com/notebook/a152282d-c148-4e58-818c-5001983f6d8a). Sete URLs foram importadas e aparecem como fontes: cinco páginas RC69 da Bíblia Online (Gênesis 1–2, Atos 17, Colossenses 1, Apocalipse 4), uma página de Gênesis da Sefaria e Colossenses 1 em grego no STEP Bible. Consulta de verificação sobre a primeira palavra hebraica de Gênesis 1:1 respondeu `בְּרֵאשִׁ֖ית` e citou a fonte. O livro RC69 não apareceu entre os dois títulos elegíveis do Google Play Livros nessa conta. Uma URL importa apenas o texto daquela página, sem percorrer seus links; o caderno ainda não equivale a uma Bíblia completa ou ao aplicativo próprio. A leitura e a qualidade de cada fonte, especialmente o alcance do texto hebraico e grego importado, precisam de avaliação adicional antes de ampliar o acervo.

**Caderno de estudo montado (27-28/10/2026), 71 fontes:**
- **Originais completos, verso a verso, com referência no padrão Almeida:** AT hebraico WLC/OSHB (7 arquivos, com Strong e glosa por palavra; títulos dos Salmos marcados; numeração hebraica indicada quando difere). NT grego (4 arquivos) com TR Scrivener 1894 e SBLGNT lado a lado, palavras do TR com Strong e glosa, e linha DIFERENÇA quando os textos divergem (pontuação e acento não contam). Fontes: OSHB (CC BY 4.0), TAGNT do STEPBible (CC BY 4.0), SBLGNT (CC BY 4.0).
- **Léxicos:** TBESH e TBESG do STEPBible (4 arquivos).
- **Comentários de domínio público (módulos SWORD da CrossWire), por versículo:** Matthew Henry Conciso, Calvino, Keil e Delitzsch (AT), Adam Clarke, Jamieson-Fausset-Brown (48 arquivos). Barnes ficou de fora (formato antigo ilegível).
- **RC69:** 6 capítulos importados por URL do site oficial da SBB (`https://www.sbb.org.br/biblia/RC69/GEN.1`, GEN.2, ACT.17, COL.1, REV.4, 1JN.5). As 5 páginas da Bíblia Online foram removidas porque entraram sem o texto dos versículos.
- **Instrução fixa ("Configurar as conversas" → Personalizado, cerca de 3 mil caracteres):** exige RC69 e original em toda passagem, citação de fonte com autor e tradição, marca [INFERÊNCIA] com o caminho do raciocínio e proíbe reconstruir a RC69 de memória.
- **Testes (Gn 1:1, Cl 1:15, 1 Jo 5:7):** original, Strong, léxico e comentários vieram certos e citando o arquivo correto, nos três. A RC69 apareceu só em Gn 1:1. Em Cl 1 e 1 Jo 5 o caderno diz que a RC69 falta: as páginas da SBB aparecem completas no visualizador, mas o NotebookLM só indexa o cabeçalho delas. Conclusão: URL de capítulo não serve como fonte confiável da RC69.
- **RC69 completa:** o ebook oficial da SBB (Google Play R$ 11,90; Amazon Kindle) tem DRM e não entra no NotebookLM. A integração Play Livros → NotebookLM só aceita títulos selecionados em inglês. Os termos da SBB (EULA §5 e §6) vedam cópia sem permissão e indicam `direitos@sbb.org.br`. Rascunho do pedido de autorização criado no Gmail de josemardp, **não enviado**, aguardando o "sim" do Josemar. Com a autorização, montar arquivo RC69 verso a verso no mesmo formato dos originais.
- **Scripts geradores** (`gerar_originais.py`, `gerar_comentarios.py`, só biblioteca padrão) ficaram no scratchpad da sessão de 27/10, fora do repositório. Decidir se entram no repo.

---

## Estado atual

Repositório Git válido, branch `main`, com a infraestrutura completa de pastas do PRD §5.2 criada, 66 fichas de livros geradas em `02-Livros/`, 4 notas-mestras de método/contexto em `00-Metodo/` e `01-Contexto/`, 1 índice tabular `01-Contexto/indice-de-povos.md`, 1 porta `08-Palavras/Amor.md`, 6 fichas de termos em `08-Palavras/`, suíte completa de templates (`nota.md`, `porta.md`, `dossie-palavra.md`, `dossie-tema.md`, `prompts.md`), painel de controle `_painel.base`, manual técnico `00-Metodo/setup.md`, suíte de integridade `_projeto/verificar.py` com 12 checks automatizados aprovados e relatório de nascimento em `_projeto/nascimento.md`.

**O que existe:**
- `CLAUDE.md`
- `_projeto/` com PRD v11, README, SPRINTS, DECISOES, STATUS, nascimento e os prompts arquivados
- `.gitignore` e `.gitattributes` (conferidos contra PRD §5.4, sem alteração)
- Repositório Git inicializado, branch `main`, commits de S0, S1, S2, S3, S4 e S5
- As 12 pastas do PRD §5.2 (10 numeradas + `_templates/` + `_inbox/`)
- `gerar_fichas.py` na raiz
- 66 fichas de livros em `02-Livros/` (frontmatter YAML completo e cabeçalhos de estudo vazios)
- 4 notas estruturais de método/contexto (`00-Metodo/hermeneutica-e-exegese-basica.md`, `00-Metodo/falacias-de-estudo-de-palavra.md`, `00-Metodo/formacao-do-canon.md`, `01-Contexto/cronologia-biblica.md`) com frontmatter e cabeçalhos vazios
- 1 índice estrutural tabular `01-Contexto/indice-de-povos.md` (tabela com cabeçalho e zero linhas)
- 1 porta em `08-Palavras/Amor.md` (`tipo: porta`, `status: rascunho`, tabela com cabeçalho e zero linhas)
- 6 fichas de termos originais em `08-Palavras/` (`ʾāhab.md`, `ḥesed.md`, `raḥam.md`, `agapē.md`, `philia.md`, `storgē.md`) com `tipo: palavra`, `status: vazio`, eixos e checklist anti-falácia
- Templates completos em `_templates/` (`nota.md`, `porta.md`, `dossie-palavra.md`, `dossie-tema.md`, `prompts.md` com D.4 e D.5 literais e completos)
- `_painel.base` com as 6 views do PRD §9 e filtro global
- `00-Metodo/setup.md` com documentação técnica do ambiente
- `_projeto/verificar.py` com os 12 checks de integridade passando com código 0 (77 notas analisadas)
- `_projeto/nascimento.md` com auditoria completa de nascimento do PRD §9
- Remoto no GitHub conectado: `origin` → https://github.com/esdraaline/BibliaOS (**público** desde 2026-09-06, D-22)
- `_projeto/guia-usuario.html` — guia visual de uso do sistema, com seção "Na Prática" contendo 3 capturas de tela reais do Obsidian (ficha aberta, painel, autocomplete de link), publicado no GitHub Pages via branch órfão `gh-pages` (não toca na estrutura do vault em `main`): https://esdraaline.github.io/BibliaOS/

**O que não existe ainda:**
- Qualquer nota de estudo bíblico com conteúdo preenchido

---

## Progresso dos sprints

| Sprint | Estado | Data | Observação |
|---|---|---|---|
| S0 — Fundação do repositório | ✅ concluído | 2026-08-04 | Ver evidência no commit `sprint(S0)` |
| S1 — Esqueleto do vault | ✅ concluído | 2026-09-04 | 66 fichas em 02-Livros/, gerar_fichas.py, nota.md e prompts.md |
| S2 — Painel, setup e testes | ✅ concluído | 2026-09-06 | _painel.base (6 views), 00-Metodo/setup.md e _projeto/verificar.py (12 checks) |
| S3 — Esqueletos de método | ✅ concluído | 2026-09-06 | 5 arquivos em 00-Metodo e 01-Contexto; D-20 (Caminho C) com checks 10-12 ativos |
| S4 — Módulo dossiê | ✅ concluído | 2026-09-06 | porta.md, dossie-palavra/tema, prompts D.4/D.5 completos, Amor.md e 6 fichas de termos |
| S5 — Auditoria de nascimento | ✅ concluído | 2026-09-06 | Relatório `_projeto/nascimento.md`; 3 aprovados, 5 reprovados (conteúdo do usuário/visual); infraestrutura 100% pronta |

---

## Pendências do Josemar (não do agente)

- [x] Criar repositório **privado** no GitHub e conectar como remoto
- [x] Instalar o Obsidian e abrir esta pasta como vault — Obsidian 1.13.7, vault aberto em `C:\projetos\bibliaos`
- [x] Ativar os plugins core Bases e Templates — ambos ativos, pasta de modelos `_templates`; nenhum plugin de comunidade habilitado (`.obsidian/plugins` não existe)
- [x] Escolher o app de captura no celular (PRD §5.4) — Google Keep, nota "Inbox BibliaOS" criada, sem sync com o vault
- [x] Abrir `_painel.base` no Obsidian e confirmar renderização visual — feito em 2026-09-06 no Obsidian 1.13.7, com captura de tela: a view Pipeline renderiza sem erro, com as 4 colunas (`file.name`, `tipo`, `status`, `ultima_revisao`) e 0 resultado, que é o esperado enquanto todas as 66 fichas estão em `status: vazio`
- [x] Digitar `[[Gn]]`, `[[Genesis]]` e `[[Gênesis]]` no Obsidian para verificar autocomplete — feito em 2026-09-07, com captura de tela real: os três resolvem para `02-Livros/Gênesis` no autocomplete (evidência embutida em `_projeto/guia-usuario.html`, seção "Na Prática")
- [ ] Fazer primeira captura no celular e triar para o desktop
- [ ] Preencher o conteúdo de `00-Metodo/falacias-de-estudo-de-palavra.md`
- [ ] Preencher a tabela da porta `08-Palavras/Amor.md`
- [ ] Executar o primeiro ciclo real de estudo / dossiê (fechar 2 notas e 1 eixo de dossiê)

---

## Bloqueios

Nenhum.

---

## Últimas decisões registradas

Ver `_projeto/DECISOES.md`. As decisões D-01 a D-16 já estão fechadas e vêm do PRD — não devem ser reabertas pelo agente. D-17 (S0): correção de inconsistências textuais herdadas do PRD v10 → v11. D-18 (S2): `verificar.py` exclui `_templates/` e `00-Metodo/setup.md` da varredura de notas; checks 4 e 5 voltaram a exigir `tipo`/`status` sempre válidos, sem exceção. D-19 (S2): sintaxe do `.base` reconciliada contra o Obsidian 1.13.7 real (`order:` em vez de `columns:`, `direction` maiúsculo, filtro global com `file.ext` e `file.hasProperty`). D-20 (S3): Caminho C implementado — 4 notas de método mantêm frontmatter completo e proteção dos checks 10–12 com exceção explícita restrita a `check_04`; `indice-de-povos.md` como tabela pura fora de `get_all_notes()`. D-21 (S4): Frontmatter dos templates de dossiê padronizado com DNA do PRD §5.3 (`status: vazio` em dossiês e `rascunho` em `porta.md`).
