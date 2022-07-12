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
  - é utilizada em operações de leitura e escrita em dispositivos I/O.
  - Em operações que sejam mais lentas e dependem de um retorno de execução, que pode ser sucesso, ou falha.
  - Em um programa que possua partes de sua execução de forma assincrona.
  - Quando a instrução assíncrona é executada, ao invés do processador ficar esperando sua conclusão ele delega a execução desta sub-tarefa a alguma outra thread ou dispositivo e continua fazendo algum outro trabalho ao invés de esperar a execução destas tarefas. Quando a sub-tarefa assíncrona finaliza a execução a thread principal é notificada e faz uso dos resultados. Isso é chamado de funções de call-back.
  - Em algumas linguagens de programação, ao invés de utilizar funções call-back são utilizados outros objetos com operações incompletas conhecidos como promisses, futures ousimplesmente tarefa (task);
  - A programação assíncrona é melhor utilizada em tarefas que exigem uso intensivo de IO, como:
    - Leitura ou escrita em bancos de dados;
    - Chamadas à Web Services (APIs);
    - Cópia, upload ou download de dados; -

### Em execução de concorrência

- Ordem de execução
  - A ordem de execução das instruções não deve gerar efeitos no resultado final.
- Recursos compartilhados
