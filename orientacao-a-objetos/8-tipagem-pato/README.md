# Aula 7 - Tipagem Pato (_Duck Typing_)

* Quando inicializamos uma variável em python, podemos começar associando a ela um tipo (por exemplo, um inteiro).
* Depois podemos fazer a mesma variável apontar para um objeto de outro tipo (por exemplo, uma string).
```python
a = 1
a = "Maria"
```
* Isso acontece porque Python é uma linguagem que possui tipagem dinâmica.
* Em linguagens com tipagem dinâmica, o tipo de uma variável é determinado em tempo de execução, ou seja, durante a execução do programa.
* Como as variáveis não ficam "presas" a um tipo específico de dado, quando definimos uma função, não conseguimos ter certeza de qual o tipo de dados que vai ser passado como parâmetro.
* Essa forma de funcionamento é um contraste com o que acontece em linguagens com tipagem estática.
* Em linguagens com tipagem estática, o tipo de uma variável é determinado em tempo de compilação, ou seja, antes da execução do programa.
* Muitas linguagens de programação não funcionam assim. Por exemplo, em Java, o tipo de uma variável é definido no momento em que ela é criada e não pode ser alterado.

```python
def processar(animal):
    animal.quack()
    animal.andar()
    animal.voar()
    animal.nadar()
```
* A função `processar` recebe um parâmetro chamado `animal`. No entanto, a função não tem como garantir que o animal é de algum tipo específico, por exemplo, o tipo `Pato`.
* A única forma de saber se o animal faz tudo que precisamos é testar se o objeto possui todos os métodos que precisamos.
* Se o objeto passado como parâmetro possuir todos os métodos que precisamos, podemos dizer que ele é um pato.
* Esse conceito é chamado de **tipagem pato** (_duck typing_).
```
Se andar como um pato, fazer quack como um pato e voar como um pato, então é um pato.
```
* Ao fazermos isso, estamos testando durante a execução do programa se o objeto passado como parâmetro possui os métodos que precisamos sem saber se isso é realmente verdade.
* Para nós, o que importa é que o objeto se comporte como um pato. Se ele se comporta como um pato, ou seja, se possui todos os métodos esperados do tipo 'Pato', então isso é o suficiente para dizer que ele é do tipo `Pato`, ao invés de checar o tipo diretamente.