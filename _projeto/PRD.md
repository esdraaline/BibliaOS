# BíbliaOS — Sistema Operacional de Estudos Bíblicos
### PRD v11

---

## Preâmbulo — Origem e Síntese do Pedido

Este documento nasceu de uma ideia inicial: transformar o estudo bíblico leigo em um projeto estruturado, provisoriamente batizado de "BíbliaOS" — um "sistema operacional de estudos bíblicos" organizado em módulos temáticos (formação do cânon, história, idiomas, povos, cultura, geografia, livros, personagens, doutrinas, exegese, hermenêutica, filosofia, arqueologia, temas, apologética, glossário, entre outros), com o objetivo de, ao final de anos de construção, ser capaz de pegar qualquer versículo da Bíblia e compreender seu contexto histórico, cultural, geográfico, linguístico e teológico.

O pedido original foi: partindo da condição de leigo em teologia, montar um plano que guiasse "do b-a-bá" de forma sistêmica — não um curso linear com início e fim, mas algo construído no dia a dia, acumulando-se como um manual pessoal completo: história bíblica, cultura dos povos bíblicos, geografia bíblica, principais personagens, principais autores, exegese, filosofia, entre outros eixos. O primeiro rascunho de PRD trazia 26 módulos paralelos, sem sequência definida, sem critério de priorização e sem estimativa realista de tempo — e foi levado para revisão com o pedido de "melhorar" e entregar a versão final em markdown.

A primeira revisão (v2) resolveu a falta de sequência: reorganizou os 26 módulos em 6 fases cronológicas, criou templates de nota, definiu o papel da IA como pesquisadora assistida (nunca fonte única) e propôs um roadmap de aproximadamente 5 anos.

Essa versão foi corrigida em seguida: o problema não era a ambição do projeto, era confundir a *construção* da ferramenta com o *uso* da ferramenta — esticando as duas coisas num único cronograma de anos. O pedido foi reformulado: não um curso de 5 anos, mas uma ferramenta robusta, fundada (planejada e construída) em poucos dias, para depois ser desenvolvida, evoluída e usada por muitos e muitos dias.

A segunda revisão (v3) respondeu a isso separando o projeto em duas naturezas: uma **Embriogênese** de escopo fechado para construir o esqueleto completo da ferramenta — pastas, templates, board, fluxo de IA, as 66 fichas de livro já existindo, ainda que vazias — e uma **Operação** de duração indefinida, guiada por cadência (não por prazo) e por uma fila de prioridade de conteúdo, não por fases com data de término.

Essa direção foi confirmada, com a adição do conceito final que faltava nomear: a ferramenta deveria funcionar como um **organismo vivo** — algo que nasce formado, cresce por metabolismo próprio, se protege de informação não verificada, se mantém em equilíbrio e, sobretudo, **se regenera**: o conhecimento adquirido depois retroalimenta o que foi escrito antes, em vez de notas ficarem congeladas como "terminadas para sempre".

A v10 acrescenta o eixo que faltava. Até aqui o organismo crescia em **extensão** — mais livros, mais personagens, mais lugares. O pedido novo é crescer em **profundidade**: escolher uma palavra (amor, fé, sabedoria) ou um tema (os filhos de Deus, o povo de Israel, salvação, arrebatamento) e dissecá-la até o fundo — etimologia, ocorrências, exegese, traduções, história da interpretação, filosofia — criando raízes profundas em cada uma. Isso vira o módulo **Dossiê** (§8), com um sistema imunológico próprio, porque o estudo de palavra é justamente onde um leigo, usando fontes perfeitamente boas, mais confiavelmente produz conclusões erradas.

A v11 fecha a última pergunta que o documento deixava em aberto: o que existe na sua mão depois de tudo isso. A resposta é §14 — o vault é a fonte, e dele saem quatro coisas, cada uma com seu gatilho.

> Histórico no Apêndice A. Auditoria adversarial no Apêndice B. Script no Apêndice C. Prompts e templates no Apêndice D.

---

## 0. Sumário Executivo

BíbliaOS é uma ferramenta pessoal para estudo sistemático da Bíblia, projetada como **organismo vivo**: nasce com estrutura completa, cresce por metabolismo diário, percebe o que acontece fora da mesa de estudo, se protege por checagem de fontes e de método, se mantém em equilíbrio por limite de trabalho em progresso e — diferente de um curso — **se regenera**.

Duas fases:

1. **Embriogênese (~4 horas efetivas):** construir o organismo. Escopo fechado, tem fim.
2. **Vida do organismo (indefinida):** crescimento por cadência e regeneração periódica. Sem prazo.

Dois vetores de crescimento:

- **Extensão** — a fila de §10: fundamentos, panorama dos 66 livros, personagens, lugares, temas.
- **Profundidade** — os **Dossiês** de §8: um mergulho estruturado numa palavra ou num tema, em eixos finitos, **um eixo por sessão, um dossiê aberto por vez**.

**O vault é a fonte, não o produto.** De um corpus em markdown saem várias coisas — consulta diária, site pessoal, caderno em PDF, cofre de longo prazo — e nenhuma delas se escreve à mão (§14).

**Tese técnica:** nenhum plugin de terceiro no caminho crítico. Obsidian de fábrica mais Git. **Tese de método (v10):** fonte boa não garante raciocínio bom — o dossiê tem um segundo sistema imunológico, contra falácia, não contra fonte inventada.

---

## 1. Missão

> Ter, desde a primeira semana, uma ferramenta robusta e viva para estudar a Bíblia de forma sistêmica — que cresça sessão após sessão, em extensão e em profundidade, e se atualize sozinha ao longo dos anos, sem nunca precisar "recomeçar o projeto".

---

## 2. Metáfora Central

Só permanecem as linhas que impõem regra executável.

| Sistema | Equivalente | Regra que impõe |
|---|---|---|
| **Esqueleto** | Pastas, templates, propriedades | Construído inteiro na Embriogênese; muda por exceção. |
| **Sistema nervoso** | Links `[[ ]]` no corpo | Nenhuma nota vira `consolidado` com zero links de saída — medido pelo Obsidian, não por campo declarado. |
| **Sistema sensorial** | Captura móvel + `_inbox/` | Fora do vault versionado (§5.4). |
| **Metabolismo** | Cadência (§11) | Máximo uma nota nova **entrando no pipeline** por dia. |
| **Raiz** | **Dossiê (§8)** | Enquanto as notas crescem em extensão, o dossiê desce. Um dossiê aberto por vez; um eixo por sessão. |
| **Sistema imunológico I — fonte** | Fonte obrigatória; a IA só cita o que consegue abrir | Fonte inacessível vira `lacuna`, nunca `fonte`. |
| **Sistema imunológico II — método** | Checklist anti-falácia do dossiê (§8.4) | Nenhum eixo de dossiê fecha sem passar pelas quatro perguntas. |
| **Homeostase** | Teto de 3 em `pesquisando`, 5 em `rascunho`, **1 dossiê aberto** | O pipeline é pequeno por projeto — é isso que dispensa qualquer detector automático de estagnação. |
| **Regeneração** | Ciclo trimestral (§6.2) | As camadas opcionais do dossiê são justamente o que a regeneração tem para fazer. |
| **Sinais vitais** | `_painel.base` (§9) | Cinco views nativas. |

---

## 3. Princípios

- **Fundação é embriogênese; conteúdo é metabolismo.**
- **Esqueleto antes de tecido.**
- **Fonte antes de conclusão.** Toda afirmação cita de onde veio, **na linha da afirmação**. O campo `fontes` é auditoria agregada, não substitui a citação inline.
- **Conexão antes de conclusão.** Nota sem link é órgão isolado.
- **A palavra não é o conceito, e a origem não é o sentido.** Dois princípios de método que o §8.4 transforma em checklist. Estão aqui porque valem para o sistema inteiro, não só para o dossiê.
- **Lacuna declarada vale mais que preenchimento inventado.**
- **Nenhum campo sem consulta que o leia.**
- **Nenhuma dependência de terceiro no caminho crítico.**
- **Limite bem posto dispensa sensor.** Antes de criar um campo, uma view ou um alerta para vigiar um descontrole, verifique se um teto não o elimina. Foi assim que a v9 apagou sete peças — e é por isso que o dossiê de §8 não tem barra de progresso.
- **Nada é definitivo. Sem prazo, com metabolismo. Captura não é compromisso.**

---

## 4. Não-Objetivos

- Não é um curso com cronograma de anos.
- Não substitui comunidade, igreja ou mentoria pastoral.
- Não tenta "resolver" debates teológicos historicamente abertos — documenta posições, com fonte, lado a lado.
- Não depende de fluência em hebraico/grego — usa ferramentas léxicas, não forma tradutor. **Um dossiê de palavra não é um curso de idioma**; é leitura assistida do aparato léxico.
- **Não transforma etimologia em significado.** A origem de uma palavra é dado histórico, não definição do que ela quer dizer numa passagem.
- Não vira curso de arqueologia nem de filosofia acadêmica — ambos entram como apoio.
- Não terceiriza à IA a verificação de fontes que ela não consegue abrir.
- **Não é um projeto de engenharia.** Todo plugin, campo ou automação novo precisa apagar um trabalho manual recorrente.
- **Não é um vault sincronizado.** Ler no celular é conveniência opcional; capturar é requisito — problemas diferentes, resolvidos separadamente (§5.4).

---

## 5. Arquitetura

### 5.1 Stack — núcleo

| Camada | Ferramenta | Natureza |
|---|---|---|
| Notas | **Obsidian** | App |
| Views e painel | **Bases** | Core, de fábrica |
| Criação de nota com DNA | **Templates** | Core |
| Busca, grafo, backlinks | **Nativos** | Core |
| Versionamento e backup | **Git** + repositório privado, **só no desktop** | Externo |
| Captura móvel | Qualquer app de nota já em uso | Fora do vault |

**Plugins de terceiros necessários: zero.** Opcionais em §5.5.

**Por que Obsidian, dito honestamente:** não pelos recursos — pela saída. O vault é uma pasta de `.md` em texto puro. Se o Obsidian acabar, o corpus abre em qualquer editor. As views se perdem; o conhecimento, não. O app é descartável, os arquivos não.

**Por que Git, dito honestamente:** por **backup fora do dispositivo**. Anos de escrita autoral num HD só é risco inaceitável. "Ver o diff da regeneração" era justificativa poética; a real é que, se o notebook morrer, o corpus não morre.

### 5.2 Estrutura de pastas

```
BibliaOS/
├── 00-Metodo/          # cânon, hermenêutica, exegese, falácias, setup
├── 01-Contexto/        # cronologia, geografia, arqueologia, povos, cultura
├── 02-Livros/          # 66 fichas, geradas na Embriogênese
├── 03-Personagens/
├── 04-Temas/           # dossiês de tema + temas menores
├── 05-Doutrinas/
├── 06-Passagens/       # capítulos e versículos — só na etapa 5 da fila (§10)
├── 07-Apologetica/     # perguntas difíceis + filosofia como apoio
├── 08-Palavras/        # portas em português + fichas por termo original
├── 09-Biblioteca/      # uma ficha por obra física lida (§7.1)
├── _templates/
├── _inbox/
├── _painel.base
├── .gitignore
└── .gitattributes
```

**`08-Glossario/` virou `08-Palavras/`.** Não é troca de rótulo. Um glossário é uma lista de definições curtas; um dossiê de palavra é uma raiz. São **o mesmo objeto em estágios diferentes do ciclo de vida**: a entrada curta de glossário é o `rascunho` da ficha, e ela vira dossiê quando o corpus a exigir. Manter duas pastas seria congelar o glossário como "pronto" — exatamente o que o princípio "nada é definitivo" proíbe.

**Tema ou doutrina?** Regra de desempate: `04-Temas/` é **uma pergunta ou um assunto** ("os filhos de Deus", "o arrebatamento"). `05-Doutrinas/` é **uma formulação sistemática** ("soteriologia", "escatologia"). Salvação como assunto é tema; soteriologia como sistema é doutrina — e uma linka a outra.

A lista de módulos do preâmbulo continua sendo checklist de cobertura, não árvore de diretórios; quem classifica é `tipo`.

### 5.3 Propriedades (o "DNA")

```yaml
---
tipo: palavra          # livro | personagem | povo | lugar | periodo | tema | doutrina |
                       # passagem | apologetica | filosofia | palavra | porta | obra
nome: agapē
aliases: [agape, G26]
status: pesquisando    # vazio | pesquisando | rascunho | em-revisao | consolidado
fontes: []
lacunas: []
termos_originais: [G26 agapē, G25 agapaō]
tags: []
ultima_revisao: null
---
```

| Campo | View que o consome |
|---|---|
| `tipo` | Filtro global; separa eixos dentro de `01-Contexto/` e `08-Palavras/` |
| `nome` | Título de card; permite nome de arquivo ≠ título |
| `aliases` | **Resolução de link** — `[[agape]]`, `[[G26]]` e `[[agapē]]` chegam à mesma ficha |
| `status` | Pipeline e todas as views |
| `fontes` | View "consolidadas sem fonte" |
| `lacunas` | View "pauta de leitura" (§7.1) |
| `termos_originais` | View "léxico pessoal" — que, com o módulo dossiê, deixa de ser curiosidade e vira o índice do trabalho de anos |
| `ultima_revisao` | View "candidatas à regeneração" |

**O módulo dossiê não acrescenta nenhuma propriedade nova** — só um valor no enum (`porta`) e dois no vocabulário de `tipo` já existente. Um dossiê é uma nota com uma estrutura de eixos no corpo; o progresso se lê abrindo a nota, não numa barra. Ver §8.5.

**Acentos não são cosmética.** Nomes de arquivo levam acento: `Gênesis.md`, `Jó.md`, `João.md`. Sem acento, `[[Gênesis]]` não resolve contra `Genesis.md` e o Obsidian oferece criar nota nova; e `Jó`/`João` colidem no autocomplete. Num sistema cujo princípio é conexão, link que não resolve é falha estrutural. Os `aliases` cobrem grafias e abreviações. Para termos originais, o mesmo vale: `agapē.md` com aliases `agape`, `G26`.

### 5.4 Sincronização

**Regra: Git é desktop. O celular não sincroniza o vault.**

Pôr o vault no celular seria colocar a dependência mais frágil a serviço da função menos crítica. Três motivos concretos:

1. **Vazamento de credencial.** Plugins de sync mobile guardam um Personal Access Token do GitHub em `.obsidian/plugins/<nome>/data.json`, em texto puro, dentro do vault. Com `.obsidian/` versionado, o token vai commitado no primeiro push.
2. **Plugins jovens, de mantenedor único** — um deles recusa suporte por escrito. Aceitável como conveniência, inaceitável no caminho crítico.
3. **Conflito de merge**, resolvido na tela do celular, que é o pior lugar possível.

Capturar no celular não exige o vault no celular: exige um lugar de escrita rápida que você leia na triagem semanal. Qualquer app de nota já em uso serve. Uma linha por captura, sem preocupação de formato.

**`.gitignore`:**
```
.obsidian/
.trash/
.DS_Store
```
Ignorar `.obsidian/` inteiro resolve três coisas: nenhum segredo commitado, nenhum binário de plugin poluindo o histórico, nenhum diff a cada movimento de painel. A contrapartida — reinstalar ao trocar de máquina — é resolvida por `00-Metodo/setup.md`, que é onde essa informação deve estar num sistema que quer sobreviver ao Obsidian.

**`.gitattributes`:**
```
* text=auto eol=lf
```
Sem isso, no Windows, cada arquivo tocado vira diff de arquivo inteiro por CRLF/LF.

**Ritual:** `git pull` ao abrir, `git add -A && git commit && git push` ao fechar.

### 5.5 Módulos opcionais — com o custo na mesa

| Módulo | Resolve | Custo declarado |
|---|---|---|
| Plugin **Git** (Vinzent03), desktop | Commit por botão | Nenhum relevante; usa Git nativo |
| Kanban (plugin ou sobre Bases) | Arrastar card | Dependência de terceiro na interface principal, para economizar cliques num pipeline de 8 itens |
| Sync do vault no celular | Ler o corpus fora de casa | PAT em disco, conflito de merge, plugin jovem. Só com `.obsidian/` ignorado e token *fine-grained* de um repositório, com validade |
| **Dataview** | Agregar checkboxes espalhados | Plugin de terceiro, hoje sobreposto ao Bases em quase tudo. **Único caso em que valeria:** somar caixas de eixo de dossiê entre notas — e §8.5 explica por que isso não é necessário |
| **Smart Connections** | Busca semântica | Reindexação contínua e cache. Removido do plano: num corpus que você mesmo escreveu, busca nativa e backlinks resolvem |

---

## 6. Ciclo de Vida da Nota

```
vazio → pesquisando → rascunho → em-revisao → consolidado
      → (regeneração, tipicamente 6–12 meses depois) → consolidado (atualizado)
```

### 6.1 Critério de fechamento

1. Toda afirmação factual tem fonte citada **na linha da afirmação**, ou está declarada em `lacunas`.
2. Pelo menos um `[[link]]` real no corpo para outra nota do sistema.
3. Um parágrafo de reflexão pessoal — seu, não da IA.
4. Tema disputado: posições principais lado a lado, com fonte, sem veredito forçado.
5. `ultima_revisao` com a data de hoje.

Para dossiês, some o critério de §8.3. Nota com lacuna aberta **pode** fechar, desde que a lacuna esteja escrita.

### 6.2 Regeneração periódica

A cada trimestre, o painel lista as `consolidado` com `ultima_revisao` mais antiga — nunca revisadas primeiro. Escolha 2–3: releia, veja se aprendeu algo que muda a ficha, feche alguma lacuna, atualize a data.

Com o módulo dossiê, a regeneração ganha um alvo natural: **as camadas opcionais** (§8.2) de dossiês já fechados no núcleo. É a resposta operacional ao "até não faltar nada" — não falta nada *do núcleo* hoje; o resto desce nos trimestres seguintes.

---

## 7. O Papel da IA

Regra fixa: **IA pesquisa e redige rascunho; você revisa e fecha.**

1. Você abre uma ficha `vazio`, uma marcada para regeneração, ou um item do `_inbox/`.
2. Pede pesquisa **restrita às fontes de §13.1**. Pressuposto explícito: a IA precisa ter acesso real à web. Sem busca, ela redige estrutura e perguntas — não afirmações com fonte.
3. A IA preenche como `rascunho`, **em paráfrase própria**, nunca transcrição longa.
4. Você revisa, fecha o que puder, escreve a reflexão, garante a conexão, muda o `status`, atualiza `ultima_revisao`.

`_templates/prompts.md`: um prompt por `tipo`, incluindo os dois prompts de dossiê do Apêndice D, e um prompt de sistema que proíbe citar obra de §13.2 como se tivesse lido.

### 7.1 O circuito da lacuna

1. A IA registra em `lacunas`: `"BDAG — leque semântico de agapē no koiné secular"`.
2. A view "Pauta de leitura" junta tudo que só um livro seu resolve, num lugar só.
3. Ao confirmar no livro, você cria ou atualiza ficha em `09-Biblioteca/` com `tipo: obra`, com página.
4. A nota de origem passa a citar **a ficha da Biblioteca** e remove o item de `lacunas`.

O sistema imunológico deixa de ser filtro e vira órgão produtivo. Com o módulo dossiê isso deixa de ser eventual e vira o motor: um estudo sério de palavra **vai** esbarrar em léxico pago, e é bom que esbarre de forma registrada.

---

## 8. Dossiês — Raízes Profundas

Um **dossiê** é o mergulho estruturado numa palavra ou num tema até o fundo do que suas fontes alcançam. É o vetor de profundidade do sistema, e opera por eixos finitos.

### 8.1 A distinção que sustenta o módulo: palavra ≠ tema ≠ palavra em português

Três objetos diferentes, três tratamentos.

**Uma palavra em português é um mapa, não um objeto de estudo.** "Amor", em português, cobre pelo menos `ʾāhab` (amar, no sentido amplo e volitivo), `ḥesed` (lealdade pactual — que quase nunca é bem traduzido por "amor"), `raḥam` (compaixão visceral), `agapē`, `philia`, `storgē`, e a ausência conspícua de `erōs` no NT. Estudar "a palavra amor" reunindo tudo isso sob o rótulo português é estudar uma **decisão de tradutor**, não um termo bíblico.

Por isso, no BíbliaOS:

- **`tipo: porta`** — a nota em português (`Amor`, `Fé`, `Sabedoria`). Não contém o estudo: contém o **mapa**. Lista os termos originais que o português cobre, o que distingue um do outro em uma linha, e linka para as fichas. É onde você entra e para onde volta.
- **`tipo: palavra`** — a ficha por **termo original** (`ḥesed`, `agapē`, `ʾemûnâ`). É aqui que mora o dossiê de palavra. Uma raiz por ficha.
- **`tipo: tema`** — o dossiê conceitual (`Os filhos de Deus`, `Salvação`, `Arrebatamento`). Um tema não é um termo: é uma pergunta, e passa por passagens que muitas vezes **não usam** o vocabulário esperado.

Isso não complica o pedido — é literalmente o que "raízes profundas" significa: a porta é o tronco visível, as fichas de termo são as raízes que descem. E resolve de saída o erro mais comum: achar que estudou o amor bíblico depois de ler as ocorrências de uma palavra grega.

### 8.2 Os eixos

Cada eixo é uma seção `##` no corpo da nota, fechada em uma sessão. **Núcleo** é o que define o dossiê como fechado; **camadas** são o material da regeneração trimestral.

#### Dossiê de palavra (`tipo: palavra`, um termo original)

**Núcleo — 6 eixos, 6 sessões**

1. **Identificação** — termo, transliteração, número Strong, classe gramatical, forma léxica, palavras da mesma família.
2. **Leque semântico** — os sentidos atestados, **e os termos vizinhos que ele não é**. O que uma palavra exclui define tanto quanto o que ela inclui.
3. **Ocorrências e distribuição** — quantas vezes, em que livros, onde se concentra e onde some. Dado factual, obtido de graça nas ferramentas de §13.1. As concentrações são pistas: um termo que aparece 90% num livro é um termo daquele autor.
4. **Uso em contexto** — 3 a 5 passagens-chave **lidas por inteiro**, não listadas. Este eixo é o antídoto do eixo 3: contagem sem leitura produz estatística sem sentido.
5. **Tradução** — como ARA, NVI, ACF e NAA vertem o termo, e **onde divergem entre si**. Divergência de tradutores é um localizador de dificuldade exegética: onde eles discordam, quase sempre há algo real para estudar.
6. **Reflexão pessoal e conexões** — o que isso muda para você, e os `[[links]]` para o resto do corpus.

**Camadas — para a regeneração**

7. **Etimologia e história da forma** — de onde a palavra veio, **com a advertência do §8.4**: é dado histórico, não definição.
8. **Uso extrabíblico** — Septuaginta, judaísmo do Segundo Templo, koiné secular, grego clássico.
9. **Desenvolvimento canônico** — o percurso AT → LXX → NT, quando aplicável.
10. **Peso teológico** — o que se construiu doutrinariamente sobre o termo, com posições lado a lado.
11. **Filosofia** — o conceito fora da Bíblia. Entra como apoio (§4), não como eixo autônomo.
12. **Distorções comuns** — o que se prega sobre essa palavra que o aparato léxico não sustenta. Escrito por você, com fonte, depois dos eixos 2 e 4. É o eixo mais útil do dossiê inteiro e só pode existir depois dos outros.

#### Dossiê de tema (`tipo: tema`)

**Núcleo — 7 eixos, 7 sessões**

1. **Delimitação** — que pergunta exatamente estou fazendo. "Os filhos de Deus" em Gn 6, em Jo 1.12 e em Rm 8 são plausivelmente **três perguntas diferentes**; decidir qual delas é o dossiê é metade do trabalho, e não decidir é a garantia de confusão.
2. **Vocabulário do tema** — quais termos originais estão envolvidos, com `[[link]]` para as fichas de palavra. **É a junta entre os dois tipos de dossiê**: temas alimentam a fila de palavras e palavras alimentam temas.
3. **Corpus de passagens** — as passagens que tratam do tema, **incluindo as que não usam o vocabulário**. Sem isso, o tema vira estudo de palavra disfarçado.
4. **Desenvolvimento canônico** — como a ideia aparece, muda e é retomada ao longo do cânon.
5. **Contexto histórico-cultural** — o que o primeiro leitor entendia por aquilo, e o que ele nunca teria entendido.
6. **Posições em disputa** — mapeadas lado a lado: quem sustenta o quê, com que texto, e qual a objeção mais forte de cada lado. Sem veredito forçado (§4). Para "arrebatamento", este eixo *é* o dossiê.
7. **Textos difíceis** — **obrigatório**: as passagens que mais atrapalham a leitura que você prefere. Um dossiê que não tem este eixo preenchido não está fechado; está torcendo.

**Camadas — para a regeneração**

8. **História da interpretação** — como leram isso ao longo dos séculos.
9. **Filosofia e apologética.**
10. **Aplicação e pregação** — inclusive as distorções correntes.

### 8.3 Critério de fechamento do dossiê

Além dos cinco itens de §6.1:

- [ ] Todos os eixos do núcleo têm conteúdo — ou uma `lacuna` declarada dizendo o que falta e onde se resolve.
- [ ] O checklist anti-falácia de §8.4 foi passado.
- [ ] Dossiê de palavra: a **porta** em português está atualizada e linka esta ficha.
- [ ] Dossiê de tema: o eixo 7 (textos difíceis) tem ao menos um texto que **incomoda de verdade**.
- [ ] As camadas não preenchidas estão listadas ao fim da nota como pauta da próxima regeneração.

"Até não faltar nada" fica assim: o núcleo é finito e fecha em 6 ou 7 sessões; as camadas são a fila permanente que a regeneração consome. O estudo nunca acaba — mas cada volta tem fim, e você sempre sabe onde parou.

### 8.4 Sistema imunológico II — contra falácia, não contra fonte

O imunológico existente barra **fonte que a IA não pode abrir**. Ele não barra nada do que segue, porque tudo isso se produz com fontes ótimas e raciocínio ruim. É aqui que um leigo bem-intencionado, com Strong e uma concordância, mais confiavelmente produz conclusão errada — e com aparência de erudição, que é o que a torna perigosa.

Quatro perguntas, obrigatórias antes de fechar qualquer eixo de dossiê:

**1. Estou tratando a origem como se fosse o sentido?**
A etimologia diz de onde a palavra veio, não o que ela significa hoje no texto. "Sincero" talvez venha de *sine cera* — isso não faz ninguém pensar em cera ao usar a palavra. O uso no contexto manda; a etimologia informa a história e, muitas vezes, só isso. Quando o eixo 7 contradisser o eixo 4, **o eixo 4 vence**.

**2. Estou empilhando todos os sentidos numa ocorrência só?**
Uma palavra com cinco sentidos atestados não carrega os cinco em cada uso. Ela carrega **um**, definido pela frase em que está. Somar o leque inteiro numa passagem — "aqui *agapē* significa amor incondicional, sacrificial, divino e eterno" — é o erro mais comum de púlpito e o mais fácil de cometer sozinho.

**3. Estou confundindo a palavra com o conceito?**
O conceito de perdão está inteiro na parábola do filho pródigo, que não usa o verbo perdoar. O amor de Deus aparece em textos sem nenhuma palavra da família de `agapē`. Se o dossiê é de **palavra**, ele estuda o termo e admite que não esgotou o conceito. Se é de **tema**, ele tem que ir aonde a palavra não está.

**4. A distinção que estou fazendo se sustenta nos dados, ou eu a trouxe pronta?**
O caso-escola é a suposta oposição rígida entre `agapē` (amor divino) e `phileō` (amor afetivo) em Jo 21 — leitura popularíssima e que o próprio uso dos dois verbos no restante do NT, e na Septuaginta, não sustenta com a limpeza com que costuma ser pregada. Regra: **antes de afirmar que dois termos se opõem, verifique se eles se substituem em algum lugar**. Se se substituem, a oposição é sua, não do texto.

Isso vira `00-Metodo/falacias-de-estudo-de-palavra.md`, escrito na Embriogênese, e vira instrução literal nos prompts do Apêndice D. Nenhum dossiê fecha sem passar pelas quatro.

### 8.5 Como o dossiê convive com a homeostase

O dossiê é a maior ameaça ao equilíbrio do sistema: é fundo, é viciante e ocuparia sozinho todas as sessões por meses, deixando os 66 livros parados. Três regras, e nenhuma peça nova:

- **Um dossiê aberto por vez.** Ele não divide slot com o teto de 3 em `pesquisando`: tem o seu, de um. Você não estuda amor e arrebatamento na mesma quinzena.
- **Um eixo por sessão.** É o que converte um desejo sem fim numa rotina com fim: o núcleo de palavra fecha em 6 sessões, o de tema em 7 — cerca de uma quinzena de estudo diário.
- **Stubs não contam como nota nova.** Abrir a porta `Amor` cria a porta e as fichas dos termos, todas `vazio`. Isso não fere o "máximo uma nota nova por dia", pela mesma razão que as 66 fichas de livro não ferem: o limite vale para o que **entra no pipeline**, não para o que nasce vazio.

**E por que não há barra de progresso.** A tentação óbvia é um campo `eixos_fechados: 3` e uma view de progresso. Isso seria um campo declarado à mão para vigiar um único objeto que já está limitado a um — exatamente o padrão que a v9 apagou sete vezes. Com um dossiê aberto, o progresso se lê abrindo a nota. **Limite bem posto dispensa sensor**, inclusive quando o sensor seria bonito.

### 8.6 Como a fila de dossiês se abastece

A fila inicial é sua: **Amor, Fé, Sabedoria** (palavras) e **Os filhos de Deus, O povo de Israel, Salvação, Arrebatamento** (temas).

Depois disso, ela **se abastece sozinha, a partir do corpus**. Quando você escreve as fichas dos livros e dos personagens, vai linkar termos naturalmente — `[[ḥesed]]`, `[[aliança]]`, `[[justiça]]`. O painel de links não resolvidos do Obsidian mostra, de graça, quais termos você já invocou e ainda não estudou, e quantas vezes. **O termo que seu próprio corpus mais cobra é o próximo dossiê.** Isso é melhor do que qualquer lista de desejos: garante que a profundidade cresça onde a extensão já pediu, e não onde a curiosidade do mês apontou.

Regra de escolha, em uma linha: entre um termo que você quer estudar e um termo que suas notas já pediram três vezes, **o segundo ganha**.

---

## 9. Embriogênese (~4h30 efetivas, escopo fechado)

**Bloco 1 (~1h) — Esqueleto.** Obsidian; Bases e Templates ativados; as 10 pastas; `.gitignore` e `.gitattributes`; `git init`; repositório privado; primeiro push.

**Bloco 2 (~30 min) — Órgãos.** Rodar o script do Apêndice C: 66 fichas com nome acentuado, aliases, seção e testamento.

**Bloco 3 (~1h30) — Conteúdo que só você escreve.** `00-Metodo/hermeneutica-e-exegese-basica.md`; **`00-Metodo/falacias-de-estudo-de-palavra.md`** (as quatro perguntas de §8.4, com um exemplo seu em cada); `00-Metodo/setup.md`; nota-mestra de cronologia; índice dos ~12 povos principais.

**Bloco 4 (~1h) — Painel, prompts, primeiro ciclo.** `_painel.base` montado pela interface; `_templates/` com os templates de nota, de porta, de dossiê de palavra e de dossiê de tema; `_templates/prompts.md` com os prompts do Apêndice D; **duas fichas reais** de `vazio` a `consolidado`.

**Bloco 5 (~30 min) — Primeira raiz.** Abrir a porta `Amor`, criar as fichas dos termos que ela mapeia (todas `vazio`) e fechar **o eixo 1** de uma delas. Não o dossiê — um eixo. O objetivo é validar o ritual "um eixo por sessão" antes de depender dele, exatamente como o Bloco 4 valida o ciclo da nota.

### O painel (`_painel.base`)

Monte pela interface e depois confira o YAML gerado — os nomes exatos de função do Bases mudam entre versões, e a interface sempre gera a forma correta da versão instalada.

| View | Tipo | Pergunta | Filtro (essência) |
|---|---|---|---|
| **Pipeline** | tabela agrupada por `status` | O que está em andamento? | `status != "vazio"` |
| **Sem fonte** | tabela | Que nota fechou sem fonte nem lacuna? | `consolidado` + `fontes` vazio + `lacunas` vazio |
| **Órgãos isolados** | tabela | Que nota fechou sem nenhum link? | `consolidado` + zero links de saída |
| **Regeneração** | tabela por `ultima_revisao` ASC | O que revisar no trimestre? | `consolidado`, limite 5 |
| **Pauta de leitura** | tabela | O que só um livro meu resolve? | `lacunas` não vazio |
| **Léxico pessoal** | tabela | Que termos originais já estudei? | `tipo == "palavra"`, mostrando `termos_originais` e `status` |

Um filtro global exclui `_templates` e `_inbox` — sem isso os templates entram na contagem e o painel mente desde o primeiro dia.

**O board saiu do núcleo.** Não há kanban nativo no Bases — só tabela, cards, lista e mapa; todo kanban é plugin de terceiro. E o que ele compra é arrastar para mudar **um enum**, num pipeline limitado a 8 itens. A view "Pipeline", agrupada por `status`, dá a mesma leitura sem plugin.

**Não há detector de nota parada.** `file.mtime` não sobrevive ao Git — clone ou pull reescreve a data de todos os arquivos, e a detecção fica cega por duas semanas, em silêncio. Mais decisivo: com no máximo 8 notas ativas e 1 dossiê, "o que travou" se responde olhando a lista.

### Critério de nascimento

- [ ] 66 fichas com acento, aliases e `status: vazio`.
- [ ] `[[Gn]]`, `[[Genesis]]` e `[[Gênesis]]` resolvem para a mesma ficha — **testado digitando**.
- [ ] As 6 views abrem com números coerentes (templates fora da conta).
- [ ] `git log` com ao menos dois commits; `git status` limpo.
- [ ] Uma captura de celular virou nota no desktop.
- [ ] Duas notas reais fechadas com fonte, link e reflexão.
- [ ] A porta `Amor` existe, mapeia ao menos quatro termos originais, e um eixo de uma das fichas está fechado.
- [ ] `00-Metodo/falacias-de-estudo-de-palavra.md` e `setup.md` escritos.

---

## 10. Fila de prioridade (extensão)

1. Fundamentos — formação da Bíblia, cânon, hermenêutica e exegese básica.
2. Panorama dos 66 livros, em nível de resumo.
3. Ferramentas de estudo — Strong, interlinear, léxicos.
4. Aprofundamento por livro, personagem, tema ou doutrina — ordem livre.
5. Estudo verso a verso — por último; depende de todo o resto existir.

Os dossiês (§8) correm **em paralelo** a esta fila, não dentro dela: são o vetor de profundidade, com fila própria (§8.6) e ritmo próprio.

---

## 11. Cadência

| Ritmo | Tempo | O quê |
|---|---|---|
| Diário | 20–30 min | **Um** dos três: avançar um eixo do dossiê aberto; avançar ou revisar uma nota da fila; capturar. Máximo uma nota nova entrando no pipeline. |
| Semanal | ~1h | Esvaziar o `_inbox/`; olhar o Pipeline; conferir os tetos (3 / 5 / 1 dossiê). |
| Trimestral | 1–2h | Regeneração (§6.2), com prioridade para **camadas de dossiês fechados no núcleo**; varrer a pauta de lacunas. |

Proporção sugerida, não regra: cerca de metade das sessões no dossiê aberto, metade na fila de extensão. Um dossiê de núcleo fecha em duas a três semanas nesse ritmo.

---

## 12. Riscos & Mitigações

| Risco | Mitigação |
|---|---|
| Embriogênese vira projeto de engenharia | Escopo em horas + "só entra o que apaga trabalho manual" |
| Sem prazo = sem ritmo | Cadência fixa (§11) |
| Vira coleção de respostas de IA | Reflexão pessoal obrigatória no fechamento |
| WIP descontrolado | Tetos de 3, 5 e 1 dossiê |
| Estase | Ciclo trimestral com fila ordenada por `ultima_revisao` |
| Órgão isolado | Verificado contra links reais, não campo declarado |
| Insight fora da sessão se perde | Captura móvel desacoplada + triagem semanal |
| Token do GitHub vazado | `.obsidian/` inteiro no `.gitignore`; sem sync mobile no núcleo |
| Plugin de terceiro abandonado | Núcleo sem plugins de terceiro |
| Link não resolve por acento | Nomes acentuados + `aliases`, testados no nascimento |
| Histórico ilegível por CRLF | `.gitattributes` com `eol=lf` |
| Script destruir fichas preenchidas | Script idempotente (Apêndice C) |
| **Dossiê engole o projeto** | Um dossiê aberto; um eixo por sessão; proporção de §11 |
| **Dossiê nunca fecha ("falta sempre algo")** | Núcleo finito de 6/7 eixos; camadas vão para a regeneração |
| **Estudo de palavra vira falácia erudita** | Checklist de §8.4, obrigatório por eixo, mais nota-mestra e prompt |
| **Estudo de palavra em português estuda o tradutor** | Dossiê ancorado no termo original; a nota em português é porta, não estudo |
| **Tema vira estudo de palavra disfarçado** | Eixo 3 do tema exige as passagens que **não** usam o vocabulário |
| **Confirmação de viés em tema disputado** | Eixo 7 (textos difíceis) obrigatório para fechar |
| `consolidado` vira carimbo subjetivo | Critério de 5 itens + §8.3 |
| Obsidian descontinuado | Markdown puro + `setup.md` como manual de reconstrução |
| **Saída vira projeto paralelo** | Gatilhos numéricos em §14; nenhuma saída se constrói antes de haver o que mostrar |
| **Conteúdo privado vaza para o site** | Publica-se apenas `status: consolidado`, menos o que tiver a tag `privado` (§14.2) |
| **Corpus inacessível à família** | Cofre trimestral em zip, fora do GitHub, sem credencial (§14.1, saída 4) |

---

## 13. Fontes de Referência

### 13.1 Pesquisáveis pela IA

- **Léxico, interlinear, concordância:** Blue Letter Bible, STEP Bible (Tyndale House), Bible Hub — Strong's, além de Thayer e Gesenius, em domínio público.
- **Grego além do NT:** Logeion / Perseus, que dão acesso livre ao Liddell-Scott-Jones — o léxico de grego clássico e helenístico. É o que permite os eixos 8 e 12 do dossiê de palavra sem depender de obra paga.
- **Fontes judaicas e texto hebraico:** Sefaria — Tanakh com Rashi, Talmud e midrash, com referência estável.
- **Texto bíblico em português:** Bible Gateway, YouVersion — ARA, NVI, ACF, NAA para o eixo de tradução.
- **Patrística e comentários em domínio público:** CCEL — base do eixo "história da interpretação".
- **Obras esgotadas em domínio público:** Archive.org.
- **Arqueologia:** parte da Biblical Archaeology Society é aberta — artigo a artigo.

**Advertência de método sobre Strong:** a Concordância de Strong é um **índice**, não um dicionário. Os verbetes são glosas do século XIX, curtas e frequentemente mais estreitas do que o uso real. Ela serve para localizar o termo e as ocorrências; não serve para decidir o que o termo significa numa passagem. Tratar glosa de Strong como definição é a porta de entrada das quatro falácias de §8.4.

### 13.2 Estudo pessoal

A IA pode apontar que um tema *provavelmente* é tratado numa destas — isso vira `lacunas`, nunca `fontes`:

- **Método (leitura prioritária, dado o módulo dossiê):** D. A. Carson, *Falácias Exegéticas*; James Barr, *The Semantics of Biblical Language*; Moisés Silva, *Biblical Words and Their Meaning*. São exatamente o antídoto contra o erro que o §8.4 descreve, escritos por quem catalogou o problema.
- **Léxicos de referência:** BDAG (grego do NT), HALOT ou BDB (hebraico). São o padrão real da área, e é onde a maioria das lacunas de dossiê vai se fechar.
- **Dicionários teológicos:** NIDNTTE / NIDOTTE. TDNT (Kittel) com ressalva declarada: é obra monumental **e** é a fonte mais influente do erro de confundir palavra com conceito — use-a sabendo disso.
- **Contexto histórico-cultural:** IVP Bible Background Commentary.
- **Atlas:** Zondervan Atlas of the Bible / Atlas Histórico e Geográfico da Bíblia.
- **Dicionário bíblico:** Novo Dicionário da Bíblia (Cultura Cristã) ou equivalente.
- **Filosofia:** dicionário reconhecido (ex.: Abbagnano) e introduções à filosofia da religião.

---

## 14. Saídas — o que se faz com o corpus

Até aqui o PRD descreveu como o conhecimento **entra** e como se mantém vivo. Falta a outra ponta: o que existe na sua mão depois de tudo isso.

**Princípio: o vault é a fonte, não o produto.** Markdown com frontmatter e links é um banco de dados em texto. De uma fonte saem várias saídas, todas geradas, nenhuma escrita à mão — e nenhuma delas exige mudar coisa alguma do que já foi decidido.

### 14.1 As quatro saídas

| # | Saída | Para quê | Ferramenta | Gatilho |
|---|---|---|---|---|
| 1 | **Consulta diária** | O uso real, 90% do valor | Obsidian no desktop | **Já existe desde o Dia 1** |
| 2 | **Site pessoal estático** | Consultar do celular, na igreja, sem sincronizar vault | Quartz + GitHub Pages, reconstruído a cada push | **~50 notas `consolidado`** |
| 3 | **Caderno de dossiê** (PDF/EPUB) | Imprimir, guardar, entregar a alguém | Pandoc | **Cada núcleo de dossiê fechado** (§8.3) |
| 4 | **Cofre de longo prazo** | Sobreviver a você, ao GitHub e à sua senha | Zip do vault em armazenamento externo | **Trimestral, junto da regeneração** |

Sobre a saída 2: o Quartz existe especificamente para vault Obsidian — entende `[[links]]`, gera backlinks e busca. **Nasce privado**, atrás de autenticação. Abrir ao público é decisão consciente e posterior, nunca o padrão.

Sobre a saída 3: o escopo certo é **um dossiê**, não o vault. "Amor" com o núcleo fechado vira um caderno de vinte páginas com começo, meio e fim. Um "grande livro do vault inteiro" seria a fotografia de um organismo vivo — e tratar isso como objetivo reintroduz exatamente o erro que a v3 corrigiu.

Sobre a saída 4: o cofre resolve um problema que um acervo de vinte anos precisa ter resolvido — se alguém da sua família precisar ler isso um dia, repositório privado com credencial sua não abre.

### 14.2 O que nunca sai

A regra de publicação usa o que já existe no DNA, sem propriedade nova:

- **Publica-se apenas `status: consolidado`.** Nada inacabado vai a público — o que é semanticamente exato, não um truque.
- **Menos o que tiver a tag `privado`.** Uma tag, não um campo novo: coerente com a regra de §5.3.
- **Nunca saem:** `_projeto/`, `_inbox/`, `_templates/`. E, dentro das notas, o campo `lacunas` fica fora do site — ele revela o que você ainda não conferiu, e é informação de oficina, não de vitrine.

### 14.3 O que **não** é saída

- **Planilha como sistema.** O conteúdo é texto conectado, não tabela. As duas exceções reais — índice do léxico pessoal e pauta de leitura — o Bases já entrega como view, e exporta CSV se algum dia precisar.
- **Google Drive como sistema.** Sem backlink, sem consulta, busca ruim dentro de markdown. Trocar Git por Drive rebaixaria a fundação. Drive **guardando o zip da saída 4** é outra coisa, e nesse papel é ótimo.
- **Um único grande livro do corpus.** Ver acima.

### 14.4 Por que isso não custa nada hoje

Nenhuma mudança de arquitetura é necessária: Quartz e Pandoc consomem markdown com frontmatter e links wiki, que é exatamente o que o vault já é. A única disciplina que as saídas exigem — nome de arquivo estável e link que resolve — **já está no PRD desde a v9** (§5.3), e foi decidida por outro motivo: os acentos e `aliases` que existem para o grafo não se estilhaçar são também o que torna o site possível.

Construir qualquer saída antes do gatilho é montar vitrine de loja vazia. Continue escrevendo notas; as saídas se ligam depois, quando houver o que mostrar.

---

## Apêndice A — Histórico de revisões

| Versão | O que mudou |
|---|---|
| v1 | 26 módulos paralelos, sem sequência nem prioridade. |
| v2 | Fases cronológicas, templates, IA assistida, roadmap de ~5 anos. |
| v3 | Separou construção (dias) de uso (indefinido). |
| v4–v5 | Consolidação do organismo vivo como princípio arquitetural. |
| v6 | Auditoria de **fidelidade** ao preâmbulo. |
| v7 | Auditoria **técnica** da stack. |
| v8 | Auditoria de **execução e peso**: enum de `status`, queries, `.gitignore`; 16 pastas → 10; circuito da lacuna; critério de fechamento. |
| v9 | Auditoria **adversarial**: núcleo sem plugins de terceiro; sync mobile desacoplado; `relacionados` e detecção de estagnação removidos; script em Python idempotente; acentos e aliases. |
| v10 | Módulo **Dossiê** (§8): vetor de profundidade, com distinção porta/palavra/tema, eixos finitos, e um **segundo sistema imunológico — contra falácia de método, não contra fonte inventada**. Zero propriedades novas. |
| **v11** | Seção **Saídas** (§14): o vault é a fonte, não o produto. Quatro saídas com gatilho, regra de publicação sem propriedade nova, e o que explicitamente não é saída. Zero mudança de arquitetura. |

---

## Apêndice B — A acusação, decisão por decisão

### B.1 Decisões que caíram (v7 → v9)

| Decisão | Acusação | Veredito |
|---|---|---|
| Sync do vault no celular via plugin de API | PAT em texto puro dentro do vault; com `.obsidian/` versionado, vai para o GitHub no primeiro push. Plugin jovem, mantenedor único. E serve à função menos crítica | Removido do núcleo; captura desacoplada |
| Board de kanban | Nenhum kanban é nativo. O que compra é arrastar para mudar um enum, num pipeline de 8 itens | Opcional; view "Pipeline" cobre |
| `relacionados: []` | Duplica o que o Obsidian já rastreia nos `[[links]]`; campo à mão para medir o que o sistema mede sozinho | Removido |
| `file.mtime` para detectar estagnação | Git não preserva mtime: clone ou pull cega a query por duas semanas, em silêncio | Removido, não substituído |
| Smart Connections a 300 notas | Número inventado para parecer decisão; corpus autoral não tem esse problema | Removido do plano |
| Dataview no núcleo | Bases nativo cobre filtros, groupBy e fórmulas | Opcional |
| Script em Bash | Ele trabalha em Windows; e já opera Python | Reescrito em Python |
| Nomes sem acento | `[[Gênesis]]` não resolve contra `Genesis.md`; `Jó`/`João` colidem | Acentos + aliases |
| Script com `>` | Rodar duas vezes destrói 66 arquivos | Idempotente |
| "3 a 5 dias" | Dia reservado é dia que o escopo cresce para preencher | Horas, em blocos |
| `.gitignore` só com `workspace.json` | Deixava entrar segredos, binários e churn | `.obsidian/` inteiro |
| Sem `.gitattributes` | CRLF/LF torna o histórico ilegível no Windows | `eol=lf` |

### B.2 Decisões que resistiram

| Decisão | Acusação | Por que resiste |
|---|---|---|
| Obsidian | Poderia ser VS Code, Logseq, Notion | Não pelo recurso, pela saída: markdown puro no disco. O app é descartável, o corpus não |
| Git | Obsidian tem File Recovery; ninguém lerá o diff de Habacuque | Sobrevive pelo **backup fora do dispositivo**, não pelo diff |
| 66 fichas vazias no dia 1 | Poluem busca e autocomplete por anos | É o que faz o link do ano 1 continuar certo no ano 5: `[[Hc]]` escrito hoje aponta para a ficha de 2029 |
| `tipo` com muitos valores | Nenhuma view filtra por valor específico | Assumiu a função das 6 pastas eliminadas; é a espinha da classificação |
| `fontes` além da citação inline | Redundante | Trabalho diferente: inline atribui, campo audita |
| A metáfora do organismo | Poderia ser enfeite | Cada linha remanescente impõe regra verificável |

### B.3 O padrão por trás dos cortes

Sete das doze quedas são o mesmo erro: uma peça criada para **vigiar** algo que uma regra de **contenção** já tornava desnecessário, ou para **declarar à mão** algo que o sistema já registrava sozinho. **Limite bem posto dispensa sensor** — critério permanente para qualquer coisa que se queira acrescentar, inclusive contra este documento.

### B.4 O módulo dossiê, contestado (v10)

| Decisão do módulo | Acusação | Veredito |
|---|---|---|
| Dossiê ancorado no **termo original**, não na palavra em português | Complica o pedido: ele disse "estudar a palavra amor", não "estudar `ḥesed`, `ʾāhab`, `agapē` e `philia` separadamente" | **Mantido.** Estudar "amor" em português é estudar uma decisão de tradutor — o rótulo português recorta um campo que o hebraico e o grego não recortam assim. A nota-porta preserva a entrada natural dele; as fichas de termo são as raízes que ele pediu. O pedido não foi contrariado, foi levado a sério |
| Novo `tipo: porta` | A v9 acabou de eliminar campos e valores supérfluos; acrescentar um enum contradiz isso | **Mantido, com justificativa de view.** A porta é o índice do léxico pessoal e o único lugar onde a relação "um português ↔ N originais" fica visível. Cumpre a regra "nenhum campo sem consulta que o leia" |
| Barra de progresso do dossiê (`eixos_fechados`) | Seria útil ver o quanto falta | **Rejeitado.** Campo declarado à mão para vigiar **um** objeto que já está limitado a um. É o padrão apagado sete vezes na v9. Com um dossiê aberto, o progresso se lê abrindo a nota |
| 12 eixos de palavra e 10 de tema | É o "curso de 5 anos" voltando por outra porta: uma lista de eixos que nunca termina | **Mantido, mas partido.** Núcleo de 6/7 eixos fecha o dossiê; as camadas viram pauta de regeneração. Sem essa divisão, o módulo reintroduziria exatamente o erro que o preâmbulo corrigiu na v3 |
| Eixo "etimologia" rebaixado para camada opcional | Ele pediu etimologia explicitamente, e em primeiro lugar | **Mantido, e é o ponto mais importante do módulo.** Etimologia é a fonte mais frequente de conclusão errada em estudo de palavra: a origem não determina o sentido. Ela permanece no dossiê — mas depois do uso em contexto, e com regra de desempate explícita: se contradisserem, o uso vence. Colocá-la no eixo 1 seria projetar o erro dentro da estrutura |
| Eixo "textos difíceis" obrigatório no tema | Adiciona atrito num dossiê já longo | **Mantido e obrigatório.** É a única peça do sistema que atua contra viés de confirmação. Num tema como arrebatamento, um dossiê sem ele não está estudando: está reunindo munição |
| `08-Glossario/` → `08-Palavras/` | Renomear pasta quebra links existentes | **Mantido**, e sem custo real: a renomeação acontece na Embriogênese, antes de existir link. Glossário e dossiê são o mesmo objeto em estágios diferentes; duas pastas congelariam o glossário como "pronto" |
| Um dossiê aberto por vez | Restringe demais quem tem vários interesses simultâneos | **Mantido.** É a única defesa contra o modo de falha mais provável deste módulo: quatro raízes de 20 cm em vez de uma de 2 m. A fila de §8.6 garante que nada se perde — só espera |

### B.5 As saídas, contestadas (v11)

| Decisão | Acusação | Veredito |
|---|---|---|
| Site com **Quartz**, um gerador de terceiro | A v9 estabeleceu "nenhuma dependência de terceiro no caminho crítico". Isto é um terceiro | **Mantido, e a regra não foi violada.** A distinção é entre dependência de **núcleo** e de **derivação**: se o Quartz sumir amanhã, o corpus não perde uma linha — só deixa de ter site até você trocar de gerador. Dependência descartável por construção não é caminho crítico |
| Site **privado por padrão** | Um site privado é quase um vault com passos a mais | **Mantido.** O vault tem lacunas declaradas e reflexão pessoal. Publicar por padrão inverteria o ônus da decisão — e essa é uma decisão que só se toma uma vez, porque o que foi indexado não se despublica |
| Publicar filtrando por `status: consolidado` | Poderia ser um campo `publicar: true`, mais explícito | **Rejeitado o campo.** Seria propriedade nova mantida à mão, contra §5.3 e contra D-08. E `consolidado` já significa exatamente "passou pelo critério de fechamento" — o filtro semântico correto já existia |
| **Drive como cofre**, não como sistema | Se Drive serve para guardar, por que não guardar tudo lá? | **Mantido nos dois sentidos.** Drive não tem backlink nem busca decente em markdown: como sistema, rebaixa a fundação. Como destino de um zip trimestral, é exatamente a camada onde ele é bom |
| **Planilhas praticamente ausentes** | Ele perguntou por planilhas explicitamente | **Mantido.** O objeto de estudo é texto conectado; tabela perde o que o sistema tem de melhor, que são os links. Onde tabela genuinamente ajuda — léxico pessoal, pauta de leitura — o Bases já entrega, e exporta CSV |
| **Gatilhos numéricos** (~50 notas, dossiê fechado, trimestre) | "50" tem o mesmo cheiro do "300 notas" que a v9 rejeitou como número inventado | **Mantido, com a diferença que importa.** O "300" era gatilho para *resolver um problema que não existia* (busca semântica em corpus autoral). Aqui o problema existe desde a primeira nota — consultar fora de casa — e o número só marca quando vale a pena o trabalho de montar. Gatilho ruim é o que nunca dispara; este dispara |
| Exportar **por dossiê**, não o vault inteiro | Ele falou em "um grande livro" | **Mantido.** Um livro do corpus inteiro é a fotografia de um organismo vivo: nasce desatualizado e convida a tratar o vault como manuscrito a terminar. O dossiê tem núcleo finito e fecha — é a única unidade do sistema que já nasce com forma de caderno |

---

## Apêndice C — Script de geração das 66 fichas

Salve como `gerar_fichas.py` na raiz do vault. Não sobrescreve nada.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria as 66 fichas de livro em 02-Livros/. Idempotente."""

from pathlib import Path

DESTINO = Path(__file__).parent / "02-Livros"

# (seção, testamento, [(nome, [aliases...]), ...])
SECOES = [
    ("Pentateuco", "AT", [
        ("Gênesis", ["Gn", "Genesis"]), ("Êxodo", ["Ex", "Exodo"]),
        ("Levítico", ["Lv", "Levitico"]), ("Números", ["Nm", "Numeros"]),
        ("Deuteronômio", ["Dt", "Deuteronomio"]),
    ]),
    ("Históricos", "AT", [
        ("Josué", ["Js", "Josue"]), ("Juízes", ["Jz", "Juizes"]), ("Rute", ["Rt"]),
        ("1 Samuel", ["1Sm"]), ("2 Samuel", ["2Sm"]), ("1 Reis", ["1Rs"]),
        ("2 Reis", ["2Rs"]), ("1 Crônicas", ["1Cr"]), ("2 Crônicas", ["2Cr"]),
        ("Esdras", ["Ed"]), ("Neemias", ["Ne"]), ("Ester", ["Et"]),
    ]),
    ("Poéticos", "AT", [
        ("Jó", ["Job"]), ("Salmos", ["Sl"]), ("Provérbios", ["Pv", "Proverbios"]),
        ("Eclesiastes", ["Ec"]), ("Cânticos", ["Ct", "Canticos", "Cantares"]),
    ]),
    ("Profetas Maiores", "AT", [
        ("Isaías", ["Is", "Isaias"]), ("Jeremias", ["Jr"]),
        ("Lamentações", ["Lm", "Lamentacoes"]), ("Ezequiel", ["Ez"]), ("Daniel", ["Dn"]),
    ]),
    ("Profetas Menores", "AT", [
        ("Oseias", ["Os"]), ("Joel", ["Jl"]), ("Amós", ["Am", "Amos"]),
        ("Obadias", ["Ob"]), ("Jonas", ["Jn"]), ("Miqueias", ["Mq"]),
        ("Naum", ["Na"]), ("Habacuque", ["Hc"]), ("Sofonias", ["Sf"]),
        ("Ageu", ["Ag"]), ("Zacarias", ["Zc"]), ("Malaquias", ["Ml"]),
    ]),
    ("Evangelhos e Atos", "NT", [
        ("Mateus", ["Mt"]), ("Marcos", ["Mc"]), ("Lucas", ["Lc"]),
        ("João", ["Jo", "Joao"]), ("Atos", ["At"]),
    ]),
    ("Cartas Paulinas", "NT", [
        ("Romanos", ["Rm"]), ("1 Coríntios", ["1Co"]), ("2 Coríntios", ["2Co"]),
        ("Gálatas", ["Gl", "Galatas"]), ("Efésios", ["Ef", "Efesios"]),
        ("Filipenses", ["Fp"]), ("Colossenses", ["Cl"]),
        ("1 Tessalonicenses", ["1Ts"]), ("2 Tessalonicenses", ["2Ts"]),
        ("1 Timóteo", ["1Tm"]), ("2 Timóteo", ["2Tm"]),
        ("Tito", ["Tt"]), ("Filemom", ["Fm"]),
    ]),
    ("Cartas Gerais e Apocalipse", "NT", [
        ("Hebreus", ["Hb"]), ("Tiago", ["Tg"]), ("1 Pedro", ["1Pe"]),
        ("2 Pedro", ["2Pe"]), ("1 João", ["1Jo"]), ("2 João", ["2Jo"]),
        ("3 João", ["3Jo"]), ("Judas", ["Jd"]), ("Apocalipse", ["Ap"]),
    ]),
]

MODELO = """---
tipo: livro
nome: {nome}
aliases: [{aliases}]
testamento: {testamento}
secao: {secao}
status: vazio
fontes: []
lacunas: []
termos_originais: []
tags: []
ultima_revisao: null
---

## Panorama

## Contexto histórico e cultural

## Estrutura

## Temas centrais

## Termos originais

## Reflexão pessoal

## Lacunas a conferir
- [ ] 
"""

def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    criados = pulados = total = 0
    for secao, testamento, livros in SECOES:
        for nome, aliases in livros:
            total += 1
            arquivo = DESTINO / f"{nome}.md"
            if arquivo.exists():
                pulados += 1
                print(f"  pulado (já existe): {arquivo.name}")
                continue
            arquivo.write_text(
                MODELO.format(
                    nome=nome, aliases=", ".join(aliases),
                    testamento=testamento, secao=secao,
                ),
                encoding="utf-8", newline="\n",
            )
            criados += 1
    print(f"\n{total} livros | {criados} criados | {pulados} pulados")
    assert total == 66, f"esperado 66 livros, encontrado {total}"

if __name__ == "__main__":
    main()
```

Três detalhes que não são estética: `encoding="utf-8"` e `newline="\n"` gravam LF mesmo no Windows, coerente com o `.gitattributes`; `if arquivo.exists(): continue` é a diferença entre rodar duas vezes por engano e perder um ano de trabalho; `assert total == 66` grita se você derrubar um livro da lista sem perceber — cânon incompleto é o único erro que este script poderia cometer em silêncio.

---

## Apêndice D — Templates e prompts do dossiê

### D.1 Template — nota-porta (`_templates/porta.md`)

```markdown
---
tipo: porta
nome: 
aliases: []
status: rascunho
fontes: []
lacunas: []
termos_originais: []
tags: []
ultima_revisao: null
---

> Esta nota é um **mapa**, não um estudo. A palavra em português cobre vários
> termos originais que não significam a mesma coisa. O estudo mora nas fichas.

## Termos que o português cobre

| Termo | Transliteração | Strong | Em uma linha, o que o distingue | Ficha |
|---|---|---|---|---|

## O que a tradução em português junta e o original separa

## O que ainda não mapeei
```

### D.2 Template — dossiê de palavra (`_templates/dossie-palavra.md`)

Cabeçalho com `tipo: palavra`, seguido das seções `## 1. Identificação` a `## 6. Reflexão pessoal e conexões` (núcleo), depois `## Camadas pendentes` listando os eixos 7 a 12 como caixas não marcadas. Fecha com:

```markdown
## Checklist anti-falácia (§8.4)
- [ ] Não tratei a origem como se fosse o sentido
- [ ] Não empilhei todos os sentidos numa ocorrência só
- [ ] Não confundi a palavra com o conceito
- [ ] Verifiquei se os termos que digo se opor chegam a se substituir em algum lugar
```

### D.3 Template — dossiê de tema (`_templates/dossie-tema.md`)

Mesmo padrão, com `## 1. Delimitação` a `## 7. Textos difíceis` (núcleo) e camadas 8 a 10 pendentes. O eixo 7 abre com a linha, literal, `> A passagem que mais atrapalha a leitura que eu prefiro é:` — para que ela não seja preenchida no automático.

### D.4 Prompt — eixo de dossiê de palavra

```
Você vai me ajudar num eixo específico de um estudo de palavra bíblica.
Eu sou leigo em teologia e não leio hebraico nem grego.

TERMO: <termo, transliteração e número Strong>
EIXO DESTA SESSÃO: <número e nome do eixo>

REGRAS INEGOCIÁVEIS
1. Use apenas fontes que você consegue de fato abrir e citar: Blue Letter Bible,
   STEP Bible, Bible Hub, Logeion/Perseus (LSJ), Sefaria, CCEL, Bible Gateway,
   YouVersion. Cite o que usou, na linha da afirmação.
2. Se o ponto depender de obra que você não pode abrir (BDAG, HALOT, NIDNTTE,
   TDNT, comentários impressos), NÃO infira o conteúdo. Escreva uma linha
   começando com "LACUNA:" dizendo o que falta e em que obra se resolve.
3. Não trate etimologia como significado. Se a origem histórica sugerir um
   sentido que o uso no contexto não confirma, diga isso explicitamente.
4. Não empilhe todos os sentidos atestados numa única ocorrência. Ao comentar
   uma passagem, indique qual sentido o contexto seleciona e por quê.
5. Não afirme oposição entre dois termos sem verificar antes se eles se
   substituem em algum lugar do corpus. Se se substituem, diga.
6. Distinga sempre: "isto é o que as fontes registram" x "isto é uma leitura
   teológica construída sobre o termo, sustentada por X e contestada por Y".
7. Parafraseie. Nada de transcrição longa de fonte.
8. Quando não houver dado suficiente, diga que não há. Não preencha.

FORMATO
- Markdown, direto, sem introdução.
- Ao final, três sugestões de [[link]] para outras notas que este eixo deveria
  conectar, e uma pergunta que este eixo deixou em aberto.
```

### D.5 Prompt — eixo de dossiê de tema

Mesma estrutura, com duas trocas:

- A regra 5 é substituída por: *"Inclua obrigatoriamente passagens que tratam do tema **sem usar** o vocabulário esperado. Se não houver nenhuma, diga por que."*
- Acrescente: *"No eixo de posições em disputa, apresente cada posição no seu ponto mais forte, com o texto que a sustenta e a objeção mais séria que ela enfrenta. Não conclua qual é a correta."*
