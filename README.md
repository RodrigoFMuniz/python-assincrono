# Python assincrono

## Caminho da execução normal do python

> - O interpretador python cria um processo no sistema operacional
> - O processo python cria a thread (linha de execução) para execução de código.

1. Source code
2. Compiler
3. Bytecode
4. Python Virtual Machine
   - Input
   - Library Modules
5. Code gets executed

## Concorrência e programação assíncrona

> Em ciência da computação, **<ins>concorrência</ins>** é a **execução** de **múltiplas instruções sequênciais** ao mesmo tempo.

### Dois tipos de concorrência

- Programação paralela
  - Divisão da terefa em pequenas sub tarefas
  - Executa em múltiplos cores do processador, de maneira simultânea.
  - Melhor utilização em tarefas que fazem uso excessivo da CPU/GPU.
    - Strings
    - Algoritmos de busca
    - Processamento gráfico
    - Algoritmo de processamento numérico
- Programação Assíncrona

### Em execução de concorrência

- Ordem de execução
  - A ordem de execução das instruções não deve gerar efeitos no resultado final.
- Recursos compartilhados
