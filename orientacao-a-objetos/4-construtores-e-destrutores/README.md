# Aula 4 - Construtores e Destrutores

## 01_construtores.py
* Nós já vimos exemplos de métodos construtores nas aulas passadas.
* Construtores são métodos especiais que são chamados durante a instanciação de um objeto.
* A função de um construstor é inicializar valores aos dados que são membros da classe quando uma instância é criada.
* O método `__init__()` é chamado construtor e é sempre chamado quando um objeto é criado.
* Se você não definir o método construtor explicitamente, o interpretador faz isso automaticamente por baixo dos panos, criando o **construtor padrão**.
* O construtor **construtor padrão** é o método `__init__(self)` que não aceita nenhum argumento além do `self`.
* O construtor também pode ser customizado para receber parâmetros. Neste caso, ele deixa de ser o construtor padrão e se torna um **construtor parametrizado**.
  * Ao declarar um construtor parametrizado, o interpretador python não cria mais outro construtor na classe.

## 02_destrutores.py
* Destrutores são métodos análogos aos construtores, só que para o objetivo oposto: eles são executados quando um objeto é destruído.
* A função de um destrutor é liberar a memória que o objeto estava usando quando ela não é mais necessária.
* Objetos desnecessários são excluídos automaticamente. Isso libera o espaço de memória conhecido como **coleta de lixo**.
* O nome de um método destrutor é `__del__(self)`.
* Assim como o construtor padrão, o destrutor é criado automaticamente pelo interpretador Python na classe e também é **chamado automaticamente**.
  * Isso tira do programador a responsabilidade sobre o gerenciamento direto da memória ocupada pelo programa.
* O destrutor é chamado quando todas as referências para o objeto são extintas ou quando a execução do programa é encerrada.
  * Quando um programa termina, o **coletor de lixo** do python destrói todos os objetos em memória. Esta é a última coisa que acontece durante a execução.
* Em geral, não é comum ver destrutores em códigos Python porque eles são executados automaticamente. Ainda assim é importante ter a noção de que eles existem, porque isso ajuda a entender melhor o que está acontecendo enquanto o seu programa está rodando.