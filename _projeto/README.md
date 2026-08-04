# BíbliaOS — como rodar este repositório

Esta pasta é **duas coisas ao mesmo tempo**: o repositório de trabalho que você abre no VS Code, e o vault que você abre no Obsidian. É a mesma pasta. Não duplique.

---

## Divisão de trabalho — leia antes de tudo

| Quem | Faz | Nunca faz |
|---|---|---|
| **Claude Code** (VS Code) | Pastas, scripts, templates, `.base`, frontmatter, verificação, commits | Escrever conteúdo de estudo |
| **IA de pesquisa** (com acesso à web) | Rascunho de nota, com fonte citável de PRD §13.1 | Fechar nota; citar obra que não pode abrir |
| **Você** | Revisar, conferir lacunas nos livros físicos, escrever a reflexão, mudar `status` | — |

O agente constrói a casa. Ele não escreve nos cadernos. Isso está gravado como regra dura em `CLAUDE.md` — se ele violar, é bug, e você reverte com `git revert`.

---

## Como começar

1. Abra esta pasta no **VS Code**.
2. Abra o Claude Code no terminal integrado.
3. Cole o conteúdo de **`_projeto/prompts/S0-abertura.md`**.
4. Ele vai ler o PRD e apresentar um plano. **Ele para e espera sua aprovação.** Você responde `pode ir`.
5. Ao terminar, ele atualiza o `STATUS.md`, faz commit e diz qual é o próximo prompt.
6. Repita com o próximo arquivo de `_projeto/prompts/`.

Se você fechar o VS Code no meio e voltar dias depois: abra `_projeto/STATUS.md`. Ele diz exatamente onde você parou e qual prompt colar.

---

## Mapa dos arquivos

| Arquivo | Para quê | Quem escreve |
|---|---|---|
| `CLAUDE.md` | Instruções permanentes do agente. Carregado automaticamente | Você (raramente) |
| `_projeto/PRD.md` | A especificação, v11. É a lei | Você, só por decisão consciente |
| `_projeto/README.md` | Este arquivo | Você |
| `_projeto/STATUS.md` | Onde o projeto está agora | O agente, ao fim de cada sprint |
| `_projeto/SPRINTS.md` | Os 6 sprints, com entregáveis e critério de aceite | Você |
| `_projeto/DECISOES.md` | Log de decisões fechadas e novas | Ambos |
| `_projeto/prompts/` | Um arquivo por sprint, pronto para colar | Você |
| `_projeto/verificar.py` | Testes automáticos do vault (criado no S2) | O agente |

---

## Por que `_projeto/` começa com underscore

Pela mesma razão de `_templates/` e `_inbox/`: agrupa a infraestrutura fora do corpus e fica fácil de excluir no filtro global do painel (PRD §9). Sem esse filtro, o `PRD.md` apareceria nas suas views como se fosse uma nota de estudo.

---

## Os sprints, em uma linha cada

| Sprint | Entrega |
|---|---|
| **S0** | Repositório válido: Git, ignores, estrutura de pastas |
| **S1** | Esqueleto do vault: templates, script, 66 fichas |
| **S2** | Painel `.base`, `setup.md` e `verificar.py` |
| **S3** | Esqueletos das notas-mestras de método (vazios, para você preencher) |
| **S4** | Módulo dossiê: templates de porta e dossiê, prompts de IA, porta `Amor` |
| **S5** | Auditoria de nascimento — aprovado ou reprovado, item por item |

**Depois do S5 não há sprint nenhum.** O organismo passa a viver por cadência (PRD §11), não por projeto. Se você se pegar planejando "S6, S7, S8", releia o preâmbulo do PRD: esse é exatamente o erro que a v3 corrigiu.

---

## O que sai disso tudo

O vault é a **fonte**, não o produto (PRD §14). Quatro saídas, cada uma com gatilho:

| Saída | Gatilho |
|---|---|
| Consulta diária no Obsidian | já existe desde o Dia 1 — é 90% do valor |
| Site pessoal estático (Quartz), privado | ~50 notas `consolidado` |
| Caderno de dossiê em PDF (Pandoc) | cada núcleo de dossiê fechado |
| Cofre em zip fora do GitHub | trimestral, junto da regeneração |

Nada disso exige mudar o vault: markdown com frontmatter e `[[links]]` já é o formato que essas ferramentas consomem. **Nenhuma saída se constrói antes do gatilho.**

---

## Quando o agente errar

- Ele escreveu conteúdo de estudo → `git revert`, e diga: *"Você violou a regra suprema do CLAUDE.md. Reverta e refaça só com cabeçalhos vazios."*
- Ele sugeriu um plugin → *"Decisão fechada, PRD Apêndice B. Núcleo sem plugins de terceiro."*
- Ele criou uma propriedade nova → *"PRD §5.3 define o DNA completo. Remova."*
- Ele pulou o plano e já executou → reverta. O passo 2 do protocolo existe para você conseguir barrar antes, não depois.
