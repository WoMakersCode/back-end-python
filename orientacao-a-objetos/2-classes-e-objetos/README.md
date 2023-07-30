# Aula 02 - Classes e Objetos

## O que é a orientação a objetos
### Slides
* Até o momento, nós vimos aqui a programação tradicional. Nela, programas são listas de instruções para o computador que definem dados (através de variáveis e tipos de dados) e trabalham com esses dados usando funções.
* Dados e funções são entidades diferentes, e que precisam ser combinadas para produzir o resultado esperado.
* Por causa dessa separação, muitas vezes a programação tradicional não nos dá uma forma muito intuitiva de representar a o mundo real.
* Isso faz com que a gente crie códigos como esse aqui.
```python
muda_canal_para_cima(televisao, canal) 
```
* A programação orientada a objetos é um **paradigma** de programação diferente dessa programação tradicional.
* Podemos pensar na programação orientada a objetos como uma forma de modelar os nossos programas como objetos. Ex: televisão é um objeto, livros, são objetos, mesas são objetos...
* Objetos tem dois componentes principais: **propriedades** e **comportamentos**.
  * Propriedades: cor, forma, pesa, tamanho, etc.
  * Comportamentos: são coisas que dá pra fazer com aquele objeto.
* Exemplo: considerando o objeto televisão:
  * Propriedades: se está ligada ou não, em qual canal está, quais são os canais máximo e mínimo que são permitidos na televisão, volume.
  * Comportamentos: mudar o canal pra cima e para baixo, ligar e desligar, aumentar e reduzir o volume.
* Na programação orientada a objeitos, as propriedades e os comportametos não ficam separados, eles ficam associados ao objeto. Isso leva a códigos desse estilo:
```python
televisao.mudar_canal_para_cima()
```
* Na programação orientada a objetos (POO), objetos não são _só_ variáveis (pedaços da memória que guardam valores). Eles também são representações de algo no mundo real (sujeito/ator), e reúnem propriedades e comportamentos desse sujeito.
* Objetos são auto-contidos e reutilizáveis:
```python
televisao.ligar()
televisao.aumentar_volume()
```
* Essa forma de modelar o mundo real cria códigos claros que mostram quem é o sujeito (**objeto**) e qual é o comportamento que está sendo invocado (**método**).
  * Métodos são funções associadas a uma classe e atuam sobre um objeto.
* POO não substitui a programação tradicional – ela te dá mais ferramentas para escrever um código limpo, conciso e legível.
* POO traz novos conceitos para a linguagem: classes, herança, encapsulamento, abstrações e polimorfismo.
* Como criar meus próprios objetos em Python? Utilizando classes.
* Classes estruturas usadas para definir um novo tipo de dados (criado pela programadora). Elas descrevem o que um objeto vai ser, mas elas não criam o objeto em si.

## televisao.py
* Classes são criadas com a palavra-chave `class`.
* Conveção para nomes de classes em Python: **PascalCasing**.
* Para instanciar um objeto de uma classe, adicionamos parênteses ao nome da classe. 
  * Uma classe pode ter várias instâncias, e cada uma delas é isolada da outra e tem seus próprios atributos e métodos.
  * Chamar um método em uma instância não altera a outra.
* Toda classe tem um método especial `__init__`, que é sempre chamado quando um novo objeto daquela classe é criado.
  * O método `__init__()` é chamado de **construtor** porque ele inicializa os valores padrão do objeto.
* O primeiro parâmetro dos métodos de uma classe é chamado de `self`. Ele representa a instância sobre a qual o método vai atuar.
  * `self` dá acesso a atributos e outros métodos daquela mesma instância.
  * Não é necessário passar o parâmetro `self` ao chamar os  métodos da classe porque o interpretador faz isso aumaticamente para nós.
  * Entretanto, não se esqueça de declarar `self` como o primeiro parâmetro de seus métodos.
* Quando chamamos o método `ligar()` em uma instância, estamos alterando o estado apenas dela. A outra televisão permanece desligada.
* Se tentamos imprimir o conteúdo do objeto, visualizamos uma representação estranha. O Python mostra o tipo do objeto e o endereço da memória em que aquele objeto foi guardado.
  * Quando imprimimos um objeto do tipo `Televisao`, o interpretador Python chama o método especial `__str__()` internamente e imprime o conteúdo retornado por esse método.
  * O método especial `__str__()` permite que nós criemos uma representação em `string` para uma instância que tenha o tipo definido pela nossa classe.
* Quando digitamos o nome da variável que contém o objeto no VSCode e incluímos o ponto final `.`, o VSCode mostra uma lista de opções de métodos e atributos relativos a nossa classe.
* No módulo `datetime` da biblioteca padrão, temos as classes `datetime`, `date` e `time`.
  * Passando o mouse em cima dos nomes no `import`, podemos ver que eles são classes.