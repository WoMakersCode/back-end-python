# Aula 5 - Atributos de visibilidade e encapsulamento

## Encapsulamento - Slides
* Em Python, todos os atributos e métodos declarados em uma classe são públicos, ou seja, podem ser acessados por outros códigos externos à classe.
* Isso não quer dizer que eles devam ser usados por quem instancia um objeto daquela classe.
* Alguns atributos e métodos só existem na classe para seu funcionamento interno. Se forem alterados, podem gerar mal funcionamento e _bugs_ no código.
* No exemplo abaixo, na classe `Quadrado` há dois atributos: `altura` e `largura`. Para que a classe de fato defina um quadrado, ela precisa ter altura e largura sempre iguais. Por isso, é interessante que quem usa a minha classe entenda que não deve mexer nesses atributos.
```python
class Quadrado:
  def __init__(self, medida):
    self.altura = medida
    self.largura = medida

  def area(self):
    return altura * largura

quadrado = Quadrado(2)
quadrado.altura = 3 # não é mais um quadrado
```
* Outro exemplo: na aula anterior, quando modelamos o funcionamento de um estacionamento, nossa classe tinha um método para buscar qual o `id` da próxima vaga livre para carros e motos. Esse método serve para auxiliar para a lógica interna da classe e também não gostaríamos que ele ficasse exposto, já que não faz sentido um usuário da classe chamar este método diretamente.
* Para indicar ao usuário quais os atributos e métodos que ele não deve alterar na classe, nós utilizamos **convenções** de nomes.
* Existem duas convenções que são utilizadas em Python para se iniciar nomes de métodos e atributos:
  * **Protegidos**: Atributos e métodos que têm seus nomes iniciados com **_** (_underscore_) não devem ser acessados pelo mundo externo a não ser que o usuário saiba exatamente o que está fazendo, ou seja, ainda pode existir algum caso de uso em que faça sentido ter acesso a esse método/atributo. Em geral, o caso de uso mais comum para acesso a membros privados é com o uso de **herança**, que vamos ver em um próxima aula.
  * **Privados**: Atributos e métodos que têm seus nomes iniciados com **__** (_underscore_ duplo) não devem ser acessados pelo mundo externo de forma nenhuma. Na prática, eles têm seus nomes alterados pelo interpretador Python mas ainda são públicos, e o que garante que eles não vão ser acessados é o bom senso do usuário da classe.
* Essas são o que nós chamamos de **regras de encapsulamento**, porque a ideia é encapsular atributos e métodos que são pertinentes a nossa classe mas não ao mundo externo.
* Em outras linguagens de programação que possuem orientação a objetos como C# e Java, temos palavras-chaves especiais para definir membros privados e protegidos, mas não em Python. Em Python nós utilizamos convenções nos nomes dos métodos.
* Se um usuário da classe quiser acessar os membros protegidos e privados, ele tem como fazer isso, mas vai estar quebrando as regras de encapsulamento, que de novo, são definidas por convenções nos nomes das variáveis.
* Existe uma forma de controlar um pouco melhor como um usuário vai acessar os atributos de uma classe, que é através de **propriedades**.
* Propriedades podem ser definidas pelo uso do _decorator_ `@property`. Esse decorator cria o método `getter` da propriedade.
* Para alterar o valor de uma propriedade externamente à classe, é preciso criar o método `setter`.

## encapsulamento.py
* A classe `Pessoa` recebe três parâmetros: nome, profissão e identidade.
* O nome de uma pessoa não é algo que costuma mudar, mas pode ser que em algum caso especial seja necessário alterá-lo. Por exemplo: alguém que se divorcia e quer alterar seu sobrenome.
  * Podemos pensar na variável nome como sendo protegida, ou seja, mostramos ao usuário que não esperamos que esse variável seja alterada.
* Já a identidade é um dado sensível e não queremos que ele fique exposto de forma nenhuma. Por isso, podemos criá-lo como um dado privado.
  * Se tentarmos alterar um atributo privado, o seu valor não vai ser alterado.
* A profissão é algo que é relativamente comum de mudar, estão criamos ela como um atributo público.
* Nota: métodos especiais do Python começam e terminam com duplo _underline_. Isso não é o mesmo do que um método privado. Métodos privados possuem duplo _underline_ apenas no começo do nome.

## propriedades.py
```python
class Quadrado:
  def __init__(self, medida):
    self.altura = medida
    self.largura = medida

  @property
  def altura(self):
    return self.__medida

  @altura.setter
  def altura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  @property
  def largura(self):
    return self.__medida

 @largura.setter
  def largura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  def area(self):
    return self.largura * self.altura
```
* A classe `Quadrado` que vimos nos slides está definida aqui, com a adição de uma validação na hora de inicializar os valores das propriedades `altura` e `largura` e alguns prints para mostrar quando os métodos _getter_ e _setter_ de cada propriedade são chamados.
* Quando criamos o objeto `quadrado`, vemos que os _setters_ são chamados.
* Quando acessamos os valores, vemos que os _getters_ são chamados.
* Se removemos um dos _setters_, não conseguimos mais alterar o valor da propriedade diretamente.
