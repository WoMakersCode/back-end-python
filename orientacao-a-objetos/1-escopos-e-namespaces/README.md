# Aula 01 - Escopos e _Namespaces_

## Módulos e namespaces
### Slide
**Módulos e Namespaces - Slide**
* Suponha que você criou alguma funções que quer poder reutilizar em arquivos diferentes do seu sistema. **Módulos** são locais onde você define os nomes e funções que quer quer fiquem visíveis para o resto do seu sistema.
* Falando tecnicamente, um módulo é um “espaço que serve para a declaração de nomes”, ou seja, um _namespace_.
* Na prática, um módulo é um arquivo Python. O nome do módulo é o nome do arquivo tirando a extensão .py.
* Em um módulo podem ser definidos componentes reutilizáveis em outros arquivos Python. Ex: variáveis, funções, classes, etc.
* Módulos nos permitem quebrar o nosso código em blocos de código menores e reutilizáveis.
* Para criar um módulo, você só precisa criar um arquivo python (.py) e escrever suas funções lá dentro.
* Cuidado: se você importar um módulo ou função cujo nome tem conflito com algum objeto definido no seu namepsace local, o objeto do seu namespace local vai sobrescrever o que foi importado.
  * Isso acontecerá se o objeto do namespace local for declarado depois daquele que foi importado.
  * Como geralmente deixamos os imports no início do arquivo, esse é o caso mais comum.

### funcoes_do_log.py
* Neste exemplo vamos criar o módulo "funcoes_do_log" (note que o nome do módulo é o nome do arquivo omitindo sua extensão).
  * Declaramos em nosso módulo um atributo e uma função.

### import.py
```python
# importar um módulo na forma de um namespace separado
import meu_modulo
meu_modulo.mostrar_mensagem('Aviso: bateria fraca.')
```
* Assim como vimos no slide, a primeira forma de importar um módulo é utilizando apenas a palavra-chave `import`.
* Ao importar o módulo desta forma, para usar o que foi declarado em nosso módulo, precisamos sempre usar a sintaxe `nome_do_modulo.atributo` ou `nome_do_modulo.funcao`.
* Na prática, precisamos sempre dizer para o interpretador de qual _namespace_ vem os itens que estamos querendo usar no namespace corrente.
  

### from_import_tudo.py
```python
# importar tudo que existe no módulo para o namespace atual
from meu_modulo import *
mostrar_mensagem('Aviso: bateria fraca.')
```
* Para importar todo o conteúdo do módulo "funcoes_do_log" para o _namespace_ local, podemos utilizar a palavra-chave `from` junto com o `import *`.
* O asterisco indica que queremos importar todo o conteúdo deste módulo.
* Não é necessário especificar o _namespace_ de onde vêm as coisas que você quer usar porque os nomes são importados para o _namespace_ corrente.
* Esse tipo de abordagem costuma não ser uma boa prática porque "polui" muito o seu ambiente trazendo vários nomes que nunca serão usados em seu programa.
* Para solucionar este problema, podemos especificar importar apenas os itens que queremos usar de um determinado módulo para o _namespace_ corrente.

### from_import_especifico.py
```python
# importar itens específicos do módulo para o namespace atual
from meu_modulo import mostrar_mensagem
mostrar_mensagem('Aviso: bateria fraca.')
```
* Para importar partes específicas do módulo "funcoes_do_log" para o _namespace_ local, podemos utilizar a palavra-chave `from` junto com o `import`.
* Ao invés de usar o asterisco, especificamos os nomes que queremos importar para o _namespace_ corrente.
* Dessa maneira, o _namespace_ corrente fica mais limpo e o "autocompletar" do VS code também :)
* Lembram do `datetime`? Quando nós usamos `from datetime import datetime`, o primeiro item é o nome do módulo e o segundo é o nome de uma classe.

### conflito.py
* Um risco de importar tudo que existe em um módulo é ter uma outra função ou variável no _namespace_ corrente com o mesmo nome.
* Neste caso, é fácil ter um bug porque você pode ao invés de usar um método, o programador acaba usando o outro.

## Pacotes
* Um **pacote** é uma coleção de módulos que foi disponibilizada publicamente.
* Pacotes são arquivos externos ao sistema que estamos desenvolvendo.
* Provavelmente todas as aplicações em que você for trabalhar precisarão usar pacotes.
* Já existem pacotes para incontáveis funcionalidades: analisar dados (pandas, numpy, matplotlib), colorir o que é impresso no terminal (colorama), lidar com geração de boletos, converter moedas, etc.
  * Na prática, antes de começar a implementar uma funcionalidade nova, sempre é bom buscar se já não existem pacotes prontos que podemos usar para fazer o que queremos.
  * O [Python Package index](https://pypi.org/) contém a lista de todos os pacotes públicos que podem ser instalados utilizando o comando `pip` no terminal.
* Importar módulos que estão em um pacote funciona da mesma forma que importar módulos criados diretamente no sistema, exceto que precisamos baixar o pacote primeiro para o ambiente.

## Instalação de pacotes - Slide
* Para instalar pacotes, a nossa instalação do Python conta com o comando `pip`
  * Importante: O comando `pip` deve ser usado no terminal, não em um script python.
* Para instalar um pacote individualmente, podemos usar `pip install [nome_do_pacote]`, ou manter um um arquivo com uma lista de todos os pacotes que são utilizados no projeto.
* Geralmente é uma boa prática manter um arquivo de pacotes necessários para fazer aquele projeto funcionar. Desta forma, outros desenvolvedores e usuários do sistema têm acesso a mesma lista.
  * O nome deste arquivo chamado costuma ser _requirements.txt_
  * O conteúdo desse arquivo é o nome de um pacote por linha
  * Para instalar as dependências listadas no arquivo _requirements.txt_, é preciso rodar no terminal o comando `pip install -r requirements.txt`

### funcoes_do_log_colorido.py
* Neste arquivo alteramos um pouco a nossa função de imprimir mensagens no log para ela imprima o nível da mensagem com a fonte colorida.
* Depois de instalar o pacote `colorama`, nós podemos importá-lo de forma semelhante ao que fizemos anteriormente.
  * O pacote exige que a função `colorama.init()` seja chamada antes do seu uso.
  * Como eu sei disso? Procurei no Google :) [veja o exemplo](https://www.delftstack.com/pt/howto/python/python-print-colored-text/)

### pacote.py
* O neste arquivo vamos importar o módulo que nós criamos e usá-lo para imprimir mensagens com o início colorido.

### Slide - Escopos de variáveis
  * Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e com variáveis externas ou globais. A diferença entre elas é a **visibilidade** ou **escopo**.
```python
variavel_global = 'global teste'
def minha_funcao():
    global variavel_global
    variavel_local = 'local_teste'
    variavel_global = 'outro valor'
```
  * Variáveis declaradas dentro de uma função não podem ser acessadas fora dela. Neste caso, dizemos que a variável é **local** porque ela só existe dentro do seu escopo, que é a delimitado pela função onde é declarada.
  * Uma variável local a uma função existe apenas dentro dela, sendo normalmente inicializada a cada chamada.
  * Não podemos acessar o valor de uma variável local fora da função que a criou e, por isso, passamos parâmetros e retornamos valores nas funções, de forma a possibilitar a troca de dados no programa.
  * Variáveis declaradas fora de qualquer função são chamadas de **globais**. Elas se encontram em um escopo que é acessível em qualquer parte do seu script e também por outros módulos.
  * Uma variável global é definida fora de uma função, pode ser vista por todas as funções do módulo e por todos os módulos que importam o módulo que a definiu.
  * Uma aplicação comum de variáveis globais é o armazenamento de valores constantes no programa, que ficam acessíveis para a todas as funções.
  * Para alterar variáveis globais dentro de funções, precisamos indicar a função que estamos querendo alterar a variável do escopo global. Caso contrário, outra variável de mesmo nome é criada dentro do escopo da função e é alterada apenas localmente.

### escopos_de_variaveis.py
  * Começamos definindo uma variável **local** na função `cardapio`. Tentar acessar a variável local `comida` fora dela vai gerar um erro.
  * Declaramos a variável `bebida` no escopo `global` do módulo, então ela pode ser vista dentro de todas as funções daquele módulo.
  * Se criarmos outra variável `bebida` dentro da função `cardapio`, na verdade estamos criando uma nova variável local, e não alterando a variável global. A variável local tem prioridade porque está declarada no escopo da função.
  * Para alterar o valor de uma variável global dentro de uma função, precisamos informar a função que vamos utilizar a variável do escopo global.
