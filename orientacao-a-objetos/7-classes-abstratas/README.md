# Aula 7 - Classes Abstratas

## Classes abstratas
* Uma classe abstrata pode ser considerada como um modelo para criar outras classes. 
* Em uma classe abstrata, nós criamos um conjunto de métodos que devem ser implementados dentro de qualquer classe filha criada a partir da classe abstrata.
* Um método abstrato é um método que tem uma declaração, mas não tem uma implementação.
* Uma classe que contém um ou mais métodos abstratos é chamada de classe abstrata.
* Não é possível instanciar uma classe abstrata diretamenta. Para criar um objeto do tipo de uma classe abstrata, precisamos instanciar uma das classes filhas.
* Enquanto estamos projetando grandes unidades funcionais, usamos uma classe abstrata. A ideia é fornecer uma interface comum para diferentes implementações de um componente, que vai ser representado pelas suas classes filhas.
* Python tem o módulo `ABC` (_Abstract Base Classes_) que fornece a funcionalidade de classes abstratas. A classe abstrata precisa herdar de `ABC` e métodos abstratos são marcados com o _decorator_ `@abstractmethod`.
* Uma classe filha derivada de uma classe abstrata precisa implementar todos os métodos e propriedades abstratas. Caso contrário, não é possível criar objetos da classe filha.

**Por que usar classes abstratas?**
* Ao criar classes abstratas, você define uma interface comum para que todas as classes filhas sigam, ou seja, as classes abstratas são usadas para definir a **API** de suas classes filhas.
* Definir uma API é uma capacidade importante na área de projeto e arquitetura de software.
* Você pode estar desenvolvendo uma biblioteca de Python que vai prover a definição de uma API que vai ser implementada por outros desenvolvedores.
* Outro caso de uso é o trabalho em uma equipe/empresa grande que vai precisar criar componentes que fazem coisas semelhantes em diferentes partes do software. Geralmente, um arquiteto define a API que deve ser seguida pelos diferentes componentes.
* Isso vai ficar mais claro com um exemplo.

## classes_abstratas.py
* Vamos supor que nós estamos desenvolvendo um jogo da franquia Pokémon.
* Pokémon é uma franquia grande e conhecida por ter vários jogos lançados. Novos jogos costumam trazer novos pokémons, que ainda não eram conhecidos anteriormente.
* O arquiteto de software precisa garantir que todas as classes que definem um pokemon sigam uma determinada API, que vai contér o ataque principal daquele pokemon, um método para garantir sua evolução e uma propriedade que guarda o seu tipo.
* A classe `BasePokemon` herda da classe `ABC` e se torna assim uma classe abstrata.
* Se tentarmos criar um objeto do tipo da classe base, não vamos conseguir.
* Criamos uma classe `Pikachu` que vai herdar de `BasePokemon`. Essa classe vai precisar definir no mínimo todos os métodos e propriedades abstratas da classe base.
* Notem que definimos sem as marcações de abstrato. Essas marcações só existem na classe base.
* Se algum dos métodos não for implementado, não conseguiremos instanciar o objeto da classe `Pikachu`.
* Novos métodos podem ser adicionados nas classes derivadas.
