# Aula 03 - Entendendo Orientação a Objetos

## Modelagem OOP - Slides
* Todo software usa a mesma série de etapas para resolver problemas:
1. **Entrada de dados**: os dados são lidos de algum lugar, que pode ser o armazenamento de dados como um sistema de arquivos ou um banco de dados.
2. **Processamento**: os dados são interpretados e possivelmente alterados para serem preparados para exibição.
3. **Saída de dados**: os dados são apresentados para que um usuário físico ou um sistema possa lê-los e interagir com eles.
* A programação orientada a objetos cria **modelos** do mundo em que os dados são operados.
* Os modelos possuem classes que representam objetos ou atores do mundo real, e como eles interagem entre si.
* Durante a fase de modelagem, você examina uma descrição de um domínio e tenta analisar o texto sobre o que ocorre.
* A primeira etapa é identificar os **atores**. Eles são chamados de atores porque atuam no domínio e executam uma ação.
  * Por exemplo, uma impressora (ator) imprime (ação).
  * Atores serão objetos no nosso programa, geralmente são substantivos que representam do mundo real.
* Em seguida, você examina as descrições dos atores e de todos os **dados** necessários para executar a ação.
* Após identificar atores, você examina o que eles fazem, que é o **comportamento**.
* Os atores são transformados em objetos, as características são codificadas como dados nos objetos e os comportamentos são funções que também são adicionadas ao objeto.
* A ideia é que os dados nos objetos podem ser alterados chamando funções nos próprios objetos.
* Também há a noção de que os objetos interagem uns com os outros para chegar a um resultado tangível, gerando uma saída para o nosso programa.
* Modelagem trata-se de aprender a identificar os atores, os dados necessários e o tipo de interação que está ocorrendo.
* Você pode modelar um sistema investigando sua descrição, que é relacionada as **regras de negócio**.

## Modelagem de um estacionamento - slides
* Vamos fazer a modelagem de um sistema de estacionamento.
* Para isso, vamos levantar os requisitos.
* Então a gente conversa com um dono de estacionamento e ele nos explica o seguinte:
  * O estacionamento é um pátio de apenas um andar. Ele possui 10 vagas.
  * Há 5 vagas para carros e 5 vagas para motos. Vagas para carro são maiores do que as vagas para motos.
  * Carros e motos são identificados por suas placas.
  * Vagas são identificadas por um número. Cada vaga tem um número identificador único.
  * Carros só podem ser estacionado em vagas específicas para carros.
  * Motos preferencialmente são estacionadas em vagas de motos, mas se não houver mais vagas exclusivas de motos disponíveis, motos podem ser estacionadas em vagas de carros.
  * É preciso ter controle sobre qual carro está em qual vaga para agilizar a saída quando o dono vem buscar.
  * É preciso saber o número de vagas livres de carro e de moto para que o estacionamento saiba se pode novos carros e motos.
* O primeiro passo é identificar os atores, ou seja, os substantivos que vão se transformar em classes no nosso sistema.
  * Estacionamento, Carro, Moto e Vaga.
* Em seguida, identificamos os atributos de cada ator.
  * Estacionamento: vagas de carro, vagas de moto, carro_para_vaga, moto_para_vaga, total_de_vagas_livres_carro, total_de_vagas_livres_moto
  * Carro: placa
  * Moto: placa
  * Vaga: identificador, tipo
* Vamos então olhar identificar quem vao ser os dados de entrada, o processamento e a saída do nosso programa:
  * Em nosso sistema, a entrada vai ser um conjunto de carros (pode ser uma lista cheia de objetos dos tipos `Carro` e `Moto`, um dicionário, etc).
  * O processamento vai cuidar do estacionamento, sendo responsável por atualizar a entrada e saída de carros.
  * Ainda precisamos de algum tipo de controle para evitar que o mesmo objeto de carro o moto seja estacionado duas vezes dentro do estacionamento. Para isso, adicionamos um atributo `estacionado` nas classes `Carro` e `Moto` que será um valor booleano atualizado pelos métodos `estacionar()` e `sair_da_vaga()`.
  * Também precisamos de uma forma de mostrar qual é o estado atual do estacionamento, que é a nossa saída. Para isso, adicionamos o método `estado_do_estacionamento()` na classe `Estacionamento`.


## estacionamento.py
* Este módulo define as classes `Estacionamento`, `Carro`, `Moto` e `Vaga` que nós discutimos.
* As classes `Carro` e `Moto` são muito semelhantes.
* A classe `Vaga` recebe em seu construtor qual é o tipo daquela vaga, e possui métodos para realizar a sua ocupação e desocupação, salvando a placa do veículo que está ocupando a vaga no momento.
* A lógica mais interessante se concentra na classe `Estacionamento`:
  * O construtor inicializa os atributos que nós vimos anteriormente.
  * Utilizamos o método `inicializar_vagas` para preencher os dicionários `vagas_carro` e `vagas_motos` com objetos do tipo `Vaga`, onde cada chave é o identificador de vaga e cada valor é um objeto do tipo `Vaga`.
  * O primeiro `id` de vaga de moto é o próximo valor inteiro depois do  último `id` da vaga de carro.
  * O método `estacionar_carro()` busca a primeira vaga de carro livre na coleção de vagas de carro.
    * Se ele não encontra nenhuma vaga livre, uma exceção é lançada.
    * Se encontra, ele atualiza todas os atributos necessários para realizar o controle de ocupação da vaga.
    * O dicionário `carro_para_vaga` mantém um dicionário para agilizar a busca de em qual vaga o carro foi estacionado. 
  * O método `estacionar_moto()` funciona de forma semelhante, mas precisa levar em conta que motos podem ser estacionadas em vagas de carro caso todas as vagas de moto já estejam ocupadas.
  * O método auxiliar `buscar_id_da_proxima_vaga_livre()` inclui a lógica para buscar vagas de carro e de moto. É nele que incluímos a lógica que tenta buscar o identificador de vagas de moto e, em seguida, de carros caso não tenhamos vagas de moto livres.
  * Os métodos `remover_carro()` e `remover_moto()` encontram em qual vaga o veículo está estacionado e atualizam os valores de atributos pertinentes a remoção de veículo da vaga.
  * Finalmente, o estado do estacionamento é mostrado através de uma `string`.
  * Adicionamos o método especial `__str(self)__` para poder imprimir o estado do estacionamento com a função `print()`.


## modelagem.py
* Agora vamos utilizar as classes que criamos para simular um sistema de estacionamento.
* Começamos incluindo todas as classes do módulo `estacionamento` no _namespace_  corrente, já que vamos utilizar todas elas.
* Criamos duas listas: uma de carros e uma de motos. Utilizamos a biblioteca `random` para gerar valores inteiros aleatórios que representem as placas dos veículos.
* Em seguida, testamos as lógicas que criamos.
