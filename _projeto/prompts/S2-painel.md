# PROMPT — Sprint S2: Painel, setup e testes

```
Sprint S2. Protocolo do CLAUDE.md. Leia _projeto/STATUS.md primeiro.

Este é o sprint que instala a rede de segurança dos próximos anos. Capriche no
verificar.py: ele é o que vai me dizer, daqui a dois anos, se o vault continua
íntegro.

<escopo>
1. _painel.base — as 6 views do PRD §9, com filtro global excluindo
   _templates, _inbox e _projeto.
2. 00-Metodo/setup.md — documentação técnica do ambiente: plugins core a
   ativar, configurações, como reconstruir do zero em máquina nova. ESTE é o
   único arquivo de 00-Metodo/ que você escreve com conteúdo, porque é
   engenharia, não estudo.
3. _projeto/verificar.py — implementar exatamente os 12 checks listados no S2
   de _projeto/SPRINTS.md. Saída legível, um check por linha, código de saída
   0 se tudo passa e 1 se algo falha. Só biblioteca padrão.
</escopo>

<aceite>
- python _projeto/verificar.py sai com código 0 e imprime os 12 checks
- cada um dos 12 checks do SPRINTS.md está implementado — liste qual função
  implementa qual check
- os checks 10, 11 e 12 passam por vacuidade hoje (não há nota consolidada).
  Prove que eles REPROVARIAM criando um caso de teste temporário, rodando,
  mostrando a falha e removendo o caso depois.
</aceite>

<atencao_base>
A sintaxe do Bases muda entre versões. Escreva o .base do jeito que você
entende do PRD, mas AVISE no relatório que preciso abrir no Obsidian e
confirmar. Se der erro, eu monto pela interface e te trago o YAML gerado para
você reconciliar. A interface é a fonte da verdade, não a sua memória.
</atencao_base>

<proibido>
- Qualquer conteúdo de estudo, inclusive em setup.md
- Sugerir ou configurar plugin de terceiro
- Tocar em .obsidian/
</proibido>

Português. ✅ por etapa. Termine com:
Próximo passo: _projeto/prompts/S3-metodo.md
```
