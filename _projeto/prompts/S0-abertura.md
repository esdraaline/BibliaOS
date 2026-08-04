# PROMPT 0 — Abertura e Sprint S0

> Cole o bloco abaixo inteiro no Claude Code, dentro desta pasta aberta no VS Code.

---

```
Você vai construir a infraestrutura do BíbliaOS. Leia CLAUDE.md antes de qualquer
coisa: ele contém as regras permanentes e o protocolo de sprint. Elas valem para
esta e para todas as próximas sessões.

<contexto>
Esta pasta é ao mesmo tempo um repositório Git e um vault Obsidian. Hoje ela
contém apenas: CLAUDE.md, .gitignore, .gitattributes e a pasta _projeto/ com
PRD.md (v11), README.md, SPRINTS.md, STATUS.md, DECISOES.md e prompts/.

Nada mais existe. Nenhuma pasta do vault, nenhuma nota, nenhum commit.

O PRD é a especificação completa e é a lei. As doze decisões de
_projeto/DECISOES.md estão fechadas e não devem ser reabertas.
</contexto>

<regra_suprema>
Você constrói o ESQUELETO. Você NUNCA escreve o TECIDO.

Pode: pastas, scripts, .gitignore, arquivos .base, frontmatter, cabeçalhos de
seção vazios, templates, documentação técnica de ambiente.

NUNCA: qualquer afirmação teológica, histórica, geográfica ou linguística.
Nenhuma definição de termo hebraico ou grego. Nenhuma lista de "principais
personagens", "principais povos" ou "principais temas". Nenhum exemplo
teológico dentro de template ou prompt.

Onde o conteúdo é do usuário, escreva no corpo, literalmente:
> A preencher pelo Josemar, com fonte. Ver PRD §7.

Em dúvida se algo é esqueleto ou tecido: é tecido. Pare e pergunte.
</regra_suprema>

<tarefa>
1. Leia, nesta ordem: CLAUDE.md, _projeto/PRD.md, _projeto/SPRINTS.md,
   _projeto/DECISOES.md, _projeto/STATUS.md.

2. Emita um relatório de leitura curto, com no máximo 12 linhas:
   - a divisão esqueleto/tecido, em uma frase, com suas palavras
   - as 5 decisões travadas do CLAUDE.md, listadas
   - qualquer contradição ou ambiguidade que você encontrou entre os documentos
     (se não encontrou nenhuma, diga isso — não invente uma para parecer atento)

3. Apresente o plano do Sprint S0, numerado, com os caminhos exatos dos arquivos
   e pastas que você vai criar ou alterar.

4. PARE. Não escreva nada no disco antes de eu responder "pode ir".
</tarefa>

<escopo_S0>
Objetivo: transformar esta pasta num repositório Git válido com a estrutura de
pastas do PRD §5.2, sem nenhuma nota.

Entregáveis:
- git init, branch main, primeiro commit
- .gitignore e .gitattributes: CONFERIR contra PRD §5.4. Eles já existem. Se
  estiverem corretos, não recrie — apenas confirme no relatório.
- As 12 pastas do PRD §5.2 (as 10 numeradas + _templates/ + _inbox/), cada uma
  com um arquivo .gitkeep vazio
- _projeto/STATUS.md atualizado conforme o passo 5 do protocolo

Critério de aceite, a ser verificado por você com evidência mostrada:
- git status limpo e git log com ao menos um commit
- git check-ignore -v .obsidian/teste confirma que .obsidian/ está ignorado
- as 12 pastas aparecem em git ls-files
- nenhum arquivo .md de conteúdo foi criado
</escopo_S0>

<proibido_neste_sprint>
- Criar repositório remoto no GitHub ou configurar remote. Isso é do usuário.
- Criar, editar ou commitar qualquer arquivo dentro de .obsidian/
- Criar qualquer nota, template, script ou arquivo .base — são S1 e S2
- Instalar qualquer dependência
- Alterar _projeto/PRD.md
</proibido_neste_sprint>

<formato_saida>
- Português do Brasil, em tudo: código, comentários, commits, relatórios.
- Emita ✅ [o que foi concluído] após cada etapa da execução.
- Faça apenas o que este sprint pede. Não adiante sprint futuro, não refatore
  além do pedido, não acrescente funcionalidade não solicitada.
- Termine a resposta com uma linha:
  Próximo passo: _projeto/prompts/S1-esqueleto.md
</formato_saida>
```

---

## O que esperar

O agente vai responder com o relatório de leitura e o plano, **e vai parar**. Se ele executar sem esperar, ele violou o protocolo — reverta e cobre.

Você responde `pode ir`. Ao final ele atualiza o STATUS, faz commit e aponta o próximo prompt.

## Antes de rodar o S1

Duas coisas suas, que o agente não pode fazer:

1. Criar o repositório **privado** no GitHub e conectar: `git remote add origin <url>` e `git push -u origin main`.
2. Abrir esta pasta no Obsidian como vault e ativar os plugins core **Bases** e **Templates**.

**Próximo:** `_projeto/prompts/S1-esqueleto.md`
