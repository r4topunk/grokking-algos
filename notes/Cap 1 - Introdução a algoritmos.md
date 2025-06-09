## Exercícios

### Busca binária

> **1.1** Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

128 / 2 = 64 / 2 = 32 / 2 = 16 / 2 = 8 / 2 = 4 / 2 = 2 / 2 = 1

Resposta:
7 etapas

Revisão:
n = 128, então realizar log(128) = 7, pois 2^7 = 128

> 1.2 Suponha que você duplique o tamanho da lista. Qual seria o número máximos de etapas agoras?

128 x 2 = 256
256 / 2 = 128 / 2 = 64...

Resposta: 8 etapas

Revisão:
log(256) = 8

### Big O

> 1.3 Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica

Resposta:
Na pior da hipóteses O(n), porque eu teria que olhar cada um dos nomes

Revisão:
Lista comum = O(n)
Lista ordenada = O(log n)

> 1.4 Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica

Resposta:
Na pior da hipóteses O(n), porque eu teria que olhar cada um dos nomes

> 1.5 Você quer ler o número de cada pessoa da agenda telefônica

Resposta:
Na pior da hipóteses O(n), porque eu teria que olhar cada um dos nomes

> 1.6 Você quer ler os números apenas dos nomes que começam com A.

Resposta:
Na pior da hipóteses O(n), porque eu teria que olhar cada um dos nomes

Revisão:
Considerando que a lista esteja ordenada de forma alfabética, seria necessário primeiro `O(log n)` para encontrar o primeiro valor com A, e depois `O(k)` para varrer todos os nomes com A, onde `k` é o número de nomes com A.

### Arrays e listas encadeadas

> 2.1 Suponha que você esteja criando um aplicativo para acompanhar as suas finanças. Todos os dias você anotará tudo o que gastou e onde gastou. No final do mês, você deverá revisar os seus gastos e resumir o quanto gastou. Logo, você terá um monte de inserções e poucas leituras. Você deverá usar um array ou uma lista para implementar esse aplicativo?

Resposta:
Vou usar uma lista encadeada, que possui tempo de gravação mais rápido e de leitura mais lento. Arrays seriam para casos onde preciso ler mais do que gravar.

> 2.2 Suponha que você esteja criando um aplicativo para anotar os pedidos dos cliente em um restaurante. Seu aplicativo precisa de uma lista de pedidos. Os garçons adicionam os pedidos a essa lista e os chefes retiram os pedidos da lista. Funciona como uma fila. Os garçons colocam os pedidos no final da fila e os chefes retiram os pedidos do começo dela para cozinhá-los. Você usaria um array ou uma lista encadeada para implementar essa lista?

Resposta:
Me parece lógico usar um array, pois eu teria que mover os cartões de qualquer jeito, mas ainda seria bom o acesso aleatório porque o chef poderia pegar o cartão do começo da fila. Mas ao mesmo tempo como é o primeiro elemento talvez a lista acabe performando melhor a operação de deleção.

Revisão:
Uma lista encadeada. Muitas inserções estão ocorrendo (garçons adicionando ordens), sendo essa uma das vantagens da lista encadeada. Você não precisa pesquisar ou ter acesso aleatório (nisso arrays são bons), pois o chef sempre pega a primeira ordem da fila.

> 2.3 Vamos analisar um experimento. Imagine que o Facebook guarda uma lista de usuários. Quando alguém tenta acessar o Facebook, uma busca é feita pelo nome do usuário. Se o nome da pessoa está na lista, ela pode continuar o acesso. As pessoas acessam o Facebook com muita frequência, então existem muitas buscas nessa lista. Presuma que o Facebook usa a pesquisa binária para procurar um nome na lista. A pesquisa binária requer acesso aleatório, você precisa ser capaz de acessar o meio da lista de nomes instantaneamente. Sabendo disso, você implementaria como um array ou uma lista encadeada?

Resposta:
Como um array, que é bom para acesso aleatório.

Revisão:
Um array ordenado. Arrays fornecem acesso aleatório, então você pode pegar um elemento do meio do array instantenamente. Isso não é possível com listas encadeadas. Para acessar o elemento central de uma lista encadeada, você deve iniciar com o primeiro elemento e seguir por todos os links até o elemento central.

> 2.4 As pessoas se inscrevem no Facebook com muita frequência também. Suponha que você decida usar um array para armazenar a lista de usuários. Quais as desvantagens de um array em relação às inserções? Em particular, imagine que você está usando a pesquisa binária para buscar os logins. O que acontece quando você adiciona novos usuários em um array?

Resposta:
É necessário mover todos os outros elementos de posição. O que faz com que o array seja muito bom para ler, mas pouco performático para manipulações.

Revisão:
Inserções em arrays são lentas. Além disso, se você estiver usando a pesquisa binária para procurar os nomes de usuário, o array precisará estar ordenado. Suponha que alguém chamado Adit B se registre no Facebook. O nome dele será inserido no final do array. Assim, você precisa ordenar o array cada vez que um nome for inserido.

> 2.5 Na verdade, o Facebook não usa nem arrays nem listas encadeadas para armazenar informações. Vamos considerar uma estrutura de dados híbrida: um array de listas encadeadas. Você tem um array com 26 slots. Cada slot do array aponta para uma lista encadeada que contém os usuários que começam com a letra A. O segundo slot aponta para a lista encadeada que contém os usuários que começam com a letra B, e assim por diante.
> Suponha que Adit B se inscreva no Facebook e você queira adicioná-lo à lista. Você via ao slot 1 do array, a seguir para a lista encadeada do slot 1, e adiciona Adit B no final. Agora, suponha que você queira procurar Zakhir H. Você vai ao slot 26, que aponta para a lista encadeada de todos os nomes começados em Z. Então, procura pela lista até encontrar o Zakhir H.
> Compara esta estrutura híbrida com arrays e listas encadeadas. É mais lento ou mais rápido fazer inserções e eliminações nesse caso? Você não precisa responder dando o tempo de execução Big(O), apenas diga se a nova estrutura de dados é mais rápida ou mais lenta do que os arrays e as listas encadeadas.

Resposta:
É mais rápida, pois combina as duas tecnologias. Utiliza arrays para dividir os blocos de nomes pela letra que inicia o nome, e usa lista encadeada para guardar o nome em si.

Revisão:
Para buscas - mais lenta do que arrays, mais rápida do que listas encadeadas. Para inserções - mais rápida do que arrays, mesmo tempo para listas encadeadas. Portanto é mais leta para buscas que os arrays, porém mais rápida ou igual às listas encadeadas para tudo. ter

> 3.1 Considerando o desenho de pilha de chamada. Quais informações você pode retirar baseando-se apenas na pilha de chamada?

Resposta:
A função de ola foi executada e está aguardando a finalização da chamada da função que pergunta como vai você. Ambas as funções possuem uma variável de nome de usuário.

> 3.2 Suponha que você acidentalmente escreveu uma função recursiva que fique executando infinitamente. Como você viu, seu computador aloca memória na pilha para cada chamada de função. O que acontece com a pilha quando a função recursiva fica executando infinitamente?

Resposta:
Continua crescendo até um estouro de memória por não ter mais espaço disponível.

