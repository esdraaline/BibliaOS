# Sprints — Embriogênese

Seis sprints, escopo fechado. Total estimado: ~4h30 de trabalho efetivo (PRD §9), das quais a maior parte é sua, não do agente.

**Regra que atravessa todos:** o agente entrega estrutura verificável. Onde o PRD pede conteúdo de estudo, o entregável do agente é o arquivo com frontmatter e cabeçalhos vazios; o conteúdo é seu.

---

## S0 — Fundação do repositório

**Objetivo:** transformar esta pasta num repositório Git válido, com a estrutura de pastas do PRD §5.2, sem nenhum conteúdo ainda.

**Entregáveis**
- `git init`, branch `main`, primeiro commit
- `.gitignore` e `.gitattributes` conferidos contra PRD §5.4 (já vêm no pacote — verificar, não recriar)
- As 10 pastas numeradas + `_templates/` + `_inbox/`, cada uma com um `.gitkeep`
- `_projeto/STATUS.md` atualizado

**Critério de aceite**
- [ ] `git status` limpo, `git log` com ao menos um commit
- [ ] `git check-ignore -v .obsidian/qualquer` confirma que `.obsidian/` está ignorado
- [ ] As 12 pastas existem e aparecem em `git ls-files`
- [ ] Nenhum arquivo `.md` de conteúdo foi criado

**O agente NÃO faz:** repositório remoto no GitHub (é você quem cria, privado, e conecta), nem qualquer arquivo dentro de `.obsidian/`.

---

## S1 — Esqueleto do vault

**Objetivo:** os órgãos formados. Templates e as 66 fichas de livro.

**Entregáveis**
- `gerar_fichas.py` na raiz, conforme PRD Apêndice C — idempotente, `assert total == 66`
- As 66 fichas em `02-Livros/`, com acento, `aliases`, `testamento`, `secao`, `status: vazio`
- `_templates/nota.md` — template genérico com o DNA completo de PRD §5.3
- `_templates/prompts.md` — **só o esqueleto de seções**; o conteúdo dos prompts vem no S4

**Critério de aceite**
- [ ] `python gerar_fichas.py` roda duas vezes seguidas: a segunda reporta 66 pulados, 0 criados
- [ ] `ls 02-Livros | wc -l` retorna 66
- [ ] Nenhum arquivo tem CRLF: `file 02-Livros/*.md` ou verificação equivalente
- [ ] Os 66 arquivos têm frontmatter YAML válido (o agente deve provar isso rodando um parser, não olhando)
- [ ] Nenhum alias duplicado entre as 66 fichas
- [ ] Nenhum cabeçalho de estudo tem texto embaixo

---

## S2 — Painel, setup e testes

**Objetivo:** os sinais vitais, e a rede de segurança que vai valer para os próximos anos.

**Entregáveis**
- `_painel.base` com as 6 views de PRD §9, e filtro global excluindo `_templates`, `_inbox` e `_projeto`
- `00-Metodo/setup.md` — documentação técnica do ambiente: plugins core a ativar, configurações, como reconstruir do zero. **Isto é o único conteúdo de `00-Metodo/` que o agente escreve**
- `_projeto/verificar.py` — os testes abaixo, saída legível, código de saída 0 ou 1

**Checks obrigatórios do `verificar.py`** (esta lista é o contrato; confira se a implementação bate):
1. As 12 pastas do PRD §5.2 existem
2. Existem exatamente 66 fichas em `02-Livros/`
3. Todo `.md` fora de `_projeto/` tem frontmatter YAML válido
4. Todo `tipo` está no enum de PRD §5.3 — nenhum valor inventado
5. Todo `status` está no enum de PRD §5.3
6. Nenhuma propriedade fora da lista de PRD §5.3 aparece em qualquer nota
7. Nenhum alias aparece em duas notas diferentes
8. Nenhum arquivo contém CRLF
9. `.obsidian/` não está rastreado pelo Git
10. Nenhuma nota `consolidado` sem `fontes` e sem `lacunas`
11. Nenhuma nota `consolidado` sem ao menos um `[[link]]` no corpo
12. Nenhuma nota `consolidado` com `ultima_revisao` nulo

Os checks 10 a 12 vão passar trivialmente hoje (não há nota consolidada) e passam a valer sozinhos daqui a meses. É de propósito.

**Critério de aceite**
- [ ] `python _projeto/verificar.py` sai com código 0 e imprime cada check
- [ ] Você abre `_painel.base` no Obsidian e as 6 views renderizam sem erro
- [ ] Nenhuma view mostra arquivo de `_templates`, `_inbox` ou `_projeto`

**Nota sobre o `.base`:** a sintaxe do Bases muda entre versões. Se o arquivo gerado der erro, monte a view pela interface do Obsidian e mande o agente reconciliar o YAML com o que a interface produziu. A interface é a fonte da verdade, não a memória do agente.

---

## S3 — Esqueletos de método

**Objetivo:** os arquivos de método existem, com a estrutura certa, prontos para você preencher.

**Entregáveis** — todos com frontmatter e cabeçalhos, corpo marcado `> A preencher pelo Josemar, com fonte.`
- `00-Metodo/hermeneutica-e-exegese-basica.md`
- `00-Metodo/falacias-de-estudo-de-palavra.md` — com as quatro perguntas de PRD §8.4 **como cabeçalhos**, e nada mais
- `00-Metodo/formacao-do-canon.md`
- `01-Contexto/cronologia-biblica.md`
- `01-Contexto/indice-de-povos.md` — tabela com colunas e **nenhuma linha**

**Critério de aceite**
- [ ] Cada arquivo tem frontmatter válido e `status: vazio`
- [ ] Zero afirmação factual em qualquer um deles — nenhum nome de povo, nenhuma data, nenhuma definição
- [ ] `verificar.py` continua passando

**Este é o sprint onde o agente mais vai querer ajudar.** Um índice de doze povos parece inofensivo e ele vai produzi-lo com prazer. É tecido, e sem fonte. Se aparecer conteúdo, reverta.

---

## S4 — Módulo dossiê

**Objetivo:** a maquinaria de profundidade (PRD §8) instalada e testada com uma raiz real.

**Entregáveis**
- `_templates/porta.md`, `_templates/dossie-palavra.md`, `_templates/dossie-tema.md` — conforme PRD Apêndice D, com os eixos como cabeçalhos e o checklist anti-falácia como caixas
- `_templates/prompts.md` completo, com os prompts D.4 e D.5 do PRD, transcritos **literalmente**
- `08-Palavras/Amor.md` — a porta, com `tipo: porta`, a tabela de mapeamento **com cabeçalho e sem linhas**
- Fichas `vazio` para os termos que a porta vai mapear, com nome, transliteração e aliases — **e nada mais**. O agente pode criar o arquivo `ḥesed.md` com `aliases: [hesed, chesed, H2617]`; **não pode** escrever o que `ḥesed` significa

**Critério de aceite**
- [ ] Os três templates existem com todos os eixos do PRD §8.2 como cabeçalhos, na ordem certa
- [ ] O checklist anti-falácia está nos dois templates de dossiê
- [ ] `08-Palavras/Amor.md` existe com a tabela vazia
- [ ] As fichas de termo existem com `status: vazio` e corpo vazio
- [ ] Nenhuma glosa, nenhuma definição, nenhum "significa"
- [ ] `verificar.py` passando

**Ponto de atenção:** a coluna "o que distingue este termo" da porta é conteúdo, e é seu. O agente entrega a tabela com cabeçalho e zero linhas.

---

## S5 — Auditoria de nascimento

**Objetivo:** dizer, com evidência, se o organismo nasceu.

**Entregáveis**
- Relatório em `_projeto/nascimento.md` percorrendo o critério de PRD §9, item por item, com a evidência de cada um
- Cada item marcado **APROVADO** ou **REPROVADO**, sem meio-termo
- Lista do que ficou pendente para você, separada do que ficou pendente para o agente

**Critério de aceite**
- [ ] Todos os itens do critério de nascimento do PRD §9 aparecem no relatório
- [ ] Nenhum item aprovado sem evidência mostrada
- [ ] O teste de resolução de link (`[[Gn]]`, `[[Genesis]]`, `[[Gênesis]]`) está marcado como **verificação humana** — o agente não pode aprová-lo sozinho, porque depende de você digitar no Obsidian e ver o autocomplete

**Se algo reprovar:** corrige e roda de novo. Não existe "aprovado com ressalva" — o critério de nascimento é binário por desenho.

---

## Depois do S5

Não há S6.

A partir daqui o sistema vive por cadência (PRD §11): 20-30 min por dia, revisão semanal, regeneração trimestral. O Claude Code volta a ser útil só para manutenção de infraestrutura — ajustar uma view, corrigir o `verificar.py`, gerar um lote de fichas de um novo tipo.

**As saídas do PRD §14 não são sprints.** Site, PDF e cofre têm gatilho próprio — ~50 notas consolidadas, dossiê fechado, trimestre — e só entram quando o gatilho dispara. Montar o site com cinco notas é vitrine de loja vazia. Quando a hora chegar, é uma sessão de Claude Code, não um projeto.

**O crescimento do corpus não é trabalho de agente.** Se você se pegar montando um sprint para "preencher os 66 livros", pare e releia o preâmbulo do PRD. Foi exatamente esse erro que a v3 corrigiu, e ele volta disfarçado de produtividade.
