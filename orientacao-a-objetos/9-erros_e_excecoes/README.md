# Aula 8 - Erros e tratamento de exceções

## erros_excecoes.py
* Erros em Python podem ser de dois tipos: **erros de sintaxe** ou **exceções**.
**Erros de sintaxe**
* Quando o interpretador encontra um erro de sintaxe, a execução do programa é interrompida imediatamente.
```python
quantidade = 10000

if(quantidade > 2999)
print("Você tem mais de 3000 dinheiros.")
```
* No exemplo acima temos dois erros: faltam os dois pontos depois da condição do `if` e a linha abaixo dele não está identada.
* Erros de sintaxe são geralmente fáceis de serem corrigidos, uma vez que você entenda o qual é o problema.
* As mensagens mais comuns são `SyntaxError: invalid syntax` e `SyntaxError: invalid token`
  * As mensagens indicam onde no programa o erro ocorreu. Na verdade, ele diz a você onde o Python notou o problema, que não é necessariamente onde está o erro.
  * Algumas vezes o erro está localizado em um ponto anterior ao indicado pela mensagem de erro, frequentemente na linha anterior
* Os erros de sintaxe mais comuns:
  * Certifique-se que você não está usando uma palavra reservada do Python (Python keyword) como nome de variável.
  * Verifique que você colocou um dois-pontos (`:`) no final do cabeçalho de cada comando composto (compound statement), incluindo laço `for`, laço `while`, comandos de seleção `if`, `elif` e `else` e declaração de funções `def`.
  * Verifique se a tabulação é consistente. Você pode tabular com espaços ou tabs mas não é aconselhável misturá-los. Cada nível deve ter a mesma quantidade de espaços ou tabs.
  * Verifique seas aspas ou apóstrofes de qualquer string no código estão emparelhados.
  * Uma falta de fecha parêntese, chave ou colchete – `(`, `{` ou `[` – faz o Python continuar com a próxima linha como parte da expressão corrente. Geralmente, um erro ocorre quase que imediatamente na próxima linha.
  * Verifique pelo clássico `=` em vez de `==` em uma condição.

**Exceções**
* Quando uma exceção acontece, o programa pode ser interrompido ou não dependendo de como ela é _tratada_.
* Quando acontece algum erro que não é relacionado a sintaxe da linguagem, mas sim a lógica da execução, esse erro é chamado de exceção.
* Exceções acontecem em tempo de execução, ou seja, durante a execução de uma linha do programa.
* Por exemplo, na aula anterior vimos como funciona a tipagem pato. 
* Se o objeto passado como parâmetro não possuir todos os métodos que precisamos, o programa vai lançar uma exceção.
* Quando a exceção não é tratada, a execução do seu programa é interrompida.
* É possível tornar o seu programa mais robusto através do tratamento de exceções. Ou seja, podemos deixar indicar no nosso código o que fazer quando uma exceção acontecer para evitar que a execução seja interrompida.
* Para isso, utilizamos as palavras chaves `try`, `catch` e `finally`.
  * Colocamos o código que pode lançar exceções dentro do bloco `try`.
  * Utilizamos o bloco `catch` para capturar e tratar qualquer exceção que possa vir a ser lançada pelo código no bloco `try`.
  * Podemos adicionar um bloco `else` com código que só vai ser executado se nenhuma exceção acontecer
  * Se existe alguma coisa que precisa ser executada indepedendo ou não do erro acontecer, podemos utilizar opcionalmente o bloco `finally`.
```python
try:
    # Algum código.... 
except:
    # Bloco opcional para lidar com uma exceção (se necessário)
else:
    # Código para ser executado se não ocorrer nenhuma exceção no try
finally:
    # Código para sempre ser executado independente de acontecer
    # alguma exceção ou não
```
* O Python possui diversos tipos de exceções que podem ser encontrados na [documentação oficial](https://docs.python.org/pt-br/3.7/library/exceptions.html#concrete-exceptions).
* Podemos lançar nossas próprias exceções no código para indicar erros de execução utilizando a palavra-chave `raise`. A mensagem do erro pode ser personalizada.
* É possível criar seus próprios tipos de exceções.

## debug.py
* O primeiro passo em depurar (_debugging_), ou seja, investigar e eliminar erros de programação, é identificar que tipo de erro você cometeu.
* A forma mais básica de debugar é utilizando o `print` para mostrar até que parte do código rodou e quais eram os valores das variáveis.
* Geralmente, os ambientes de desenvolvimento oferecem suas próprias ferramentas de debug. A outra forma de debugar é utilizando a ferramenta de debug do VSCode.
* Exemplo de código: considere que você trabalha para um banco e está criando um aplicativo que monitore o valor do saldo da conta de um cliente. Este cliente recebe o salário em sua conta e o banco precisa processar o valor bruto para reter o valor referente ao imposto de renda. Depois, se o cliente quiser sacar, o banco precisa controlar o valor do saque para não permitir que o cliente gaste mais do que o valor que existe em sua conta. Seu programa usa o módulo `conta_bancaria`, que contém as seguintes funções:
  * `imprimir_no_log` para mostrar mensagens coloridas
  * `calcular_inss` e `calcular_imposto_de_renda` para que calcular os valores de impostos
  * `processar_salario`, que deve rodar apenas da primeira vez que o usuário tentar sacar o valor para retenção dos valores pagos na fonte
  * `sacar_na_conta`, que faz o saque e retorna um boolean indicando se a operação funcionou corretamente.
* O módulo também contém variáveis que indicam o saldo inicial da conta, o valor do salário bruto e o estado do processamento do salário.
* Erros no código:
  1. faltou colocar o namespace "conta_bancaria" para chamar a função "sacar na conta"
  2. Função "sacar_na_conta": variável 'valor_na_conta' é local - não disse para a função que estava usando a variável global
  3. Mesmo erro na funcao 'processar_salario'
  4. Expressão do 'processar_salario' usando o valor errado
  5. `if valor_na_conta <= valor:` -> lógica invertida
  6. Faltou atualizar a variável `salario_processado` que está sendo repetida
