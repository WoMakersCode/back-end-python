# Aula 6 - Herança e Herança Múltipla

## heranca.py
* A classe `Estudante` herda da classe `Pessoa`. A sintaxe para indicar isso é colocar o nome da "classe pai" dentro de um parênteses na frente do nome da "classe filha".
* Os métodos e variáveis da classe pai podem ser acessados com a função `super()`.
* É uma boa prática sempre chamar o construtor da classe pai no construtor da classe filha. É ele que garante que as propriedades da classe pai vão ser inicializadas corretamente.
* A classe `Estudante` herda os métodos e as propriedades públicas e protegidas da classe `Pessoa`.
* A classe `Estudante` pode sobrescrever os valores que foram herdados.
* Python provê funções nativas para testar se um objeto é instância de uma determinada classe, e se uma classe é derivada de outra.
* A classe `Trabalhador` também herda de `Pessoa`, e a classe `Professor` herda de trabalhador.
* `Professor` é um `Trabalhador` e também é uma `Pessoa`, portanto herda métodos e atributos de ambos.
* Atributos privados não podem ser alterados em classes filhas.
* Em Python, todas as classes herdam da classe `object`. Isso faz com que toda classe já comece com vários métodos e atributos.
* A função `dir()` mostra os atributos e métodos de um determinado objeto ou classe. Notem que as propriedades privadas aparecem aqui também, mas com nomes diferentes.

# Herança múltipla - Slide
* Em Python, uma classe pode herdar de mais de uma classe pai. Esse conceito é conhecido como herança múltipla.
* As vezes, classes que herdam de mais de uma classe são chamadas de **mixins**.
* Heraça múltipla é uma funcionalidade muito controversa, porque o uso dessa funcionalidade traz potencialmente muita complexidade para o código.
* Na maior parte das vezes onde alguém tenta resolver um problema com herança múltipla, existiriam soluções melhores e mais simples.
* O caso de uso mais legítimo é na criação de um _framework_.
* Ao trabalhar com Django, vocês podem ver casos onde uma classe vai herdar de duas ou mais classes.

# heranca_multipla.py
* A classe `Logavel` define o método `logar`. Qualquer classe que herdar dela vai conseguir escrever uma mensagem no log e nós vamos saber de onde a mensagem está vindo pelo atributo `nome_da_classe` que é inicializado no construtor.
  * Ter uma classe assim é interessante porque a lógica de criar um arquivo de log, escrever as mensagens dentro dele e fechar o arquivo depois fica todo em um lugar só.
  * Quem está escrevendo um software não precisa se preocupar em escrever essa lógica toda vez, é só herdar de `Logavel`.
* A classe `Conexao` serve para conectar a um servidor de banco de dados.
  * O servidor costuma ser um endereço de IP com uma porta.
* A classe `MySqlDatabase` é uma classe de exemplo que se conecta ao banco de dados **MySql**, que herda tanto de conexão quanto de logável.
* O meu `framework` super chique aqui é só um metódo que recebe um objeto chamado `item` e testa se esse objeto é uma instância de cada uma das classes. Ele só chama os métodos pertinentes se for.