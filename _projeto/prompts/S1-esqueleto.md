# PROMPT — Sprint S1: Esqueleto do vault

```
Sprint S1. Siga o protocolo de sprint do CLAUDE.md, começando por ler
_projeto/STATUS.md para confirmar que o S0 está concluído.

A REGRA SUPREMA continua valendo: esqueleto sim, tecido nunca. Uma ficha de
livro sai com frontmatter preenchido e cabeçalhos de seção VAZIOS. Zero
afirmação sobre autoria, data, tema ou conteúdo de qualquer livro bíblico.

<escopo>
1. Criar gerar_fichas.py na raiz, conforme PRD Apêndice C. Transcreva o script
   do PRD. Se você encontrar um erro real nele, PARE e me mostre antes de
   corrigir — não corrija em silêncio.
2. Rodar o script. Conferir as 66 fichas em 02-Livros/.
3. Criar _templates/nota.md com o DNA completo do PRD §5.3 e os cabeçalhos
   genéricos, corpo marcado como "A preencher".
4. Criar _templates/prompts.md apenas com os cabeçalhos das seções (um por
   tipo de nota). O conteúdo dos prompts é do S4 — deixe vazio.
</escopo>

<aceite>
Verifique cada item com evidência mostrada, não com afirmação:
- python gerar_fichas.py rodado DUAS vezes: a segunda reporta 66 pulados, 0 criados
- 02-Livros/ tem exatamente 66 arquivos
- os 66 têm frontmatter YAML válido — prove rodando um parser, não olhando
- nenhum alias se repete entre as 66 fichas — prove com código
- nenhum arquivo tem CRLF
- nenhum cabeçalho de estudo tem texto embaixo
</aceite>

<proibido>
- Preencher qualquer seção de qualquer ficha
- Criar nota fora de 02-Livros/ e _templates/
- Acrescentar propriedade ao frontmatter além do PRD §5.3
- Instalar dependência: só biblioteca padrão do Python
</proibido>

Português em tudo. ✅ após cada etapa. Termine com:
Próximo passo: _projeto/prompts/S2-painel.md
```
