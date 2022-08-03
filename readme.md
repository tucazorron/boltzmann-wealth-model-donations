# Boltzmann Wealth Model

Artur Filgueiras Scheiba Zorron - 180013696

## Apresentação

O modelo computacional de riqueza de Boltzmann é um modelo dinâmico de equilíbrio de riqueza. Sua ideia inicial de equilíbrio econômico é que os agentes do modelo randomicamente selecionem com quais outros agentes eles irão trocar riqueza. A cada passo na simulação, calcula-se o índice Gini.

O modelo computacional de riqueza de Boltzmann proposto por mim é um modelo dinâmico de equilíbrio de riqueza porém um pouco distinto do original. Neste novo modelo, existe uma probabilidade de doação de riqueza entre os agentes. Caso a doação aconteça em alguma troca monetária, o agente com menos dinheiro recebe metade da diferença monetária entre ele e o agente com mais dinheiro. Em outras palavras, quando uma doação ocorre, os dois agentes terminam com o mesmo montante de dinheiro. Pode ter um erro de 1 moeda nesse cálculo. E a cada passo da simulacão, calcula-se o índice Gini com o desvio padrão da riqueza dos agentes.

## Hipótese causal

A hipótese causal que quero comprovar é de que quanto maior a cultura de doação em uma sociedade, maior a probabilidade de que a riqueza dos agentes seja equilibrada levando a uma sociedade menos desigual com um menor índice Gini e um menor desvio padrão da riqueza dos agentes.

## Alterações no código

Adicionei duas variáveis para o modelo: uma independente e uma dependente.

Independente: Probabilidade de doação de riqueza. Varia de 0 a 1, em intervalos de 0.1. Indica a probabilidade de doação de riqueza.

Dependente: Desvio padrão da riqueza dos agentes. Indica o desvio padrão da riqueza dos agentes.

## Como usar o simulador

Instale os pacotes:

- jupyter
- matplotlib
- mesa
- numpy

Execute o comando `make` para executar o simulador.
