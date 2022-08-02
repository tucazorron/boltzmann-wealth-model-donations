# Boltzmann Wealth Model

Artur Filgueiras Scheiba Zorron - 180013696

## Apresentação

O modelo inicial de riqueza de Boltzmann é um modelo dinâmico de equilíbrio de riqueza. Sua ideia inicial de equilíbrio econômico é que os agentes do modelo randomicamente selecionem com quais outros agentes eles irão trocar riqueza. Com estas trocas, calcula-se o índice de Gini para entender quão desigual é esta sociedade.

O novo modelo de riqueza de Boltzmann é um modelo dinâmico de equilíbrio de riqueza porém um pouco distinto do original. Enquanto o modelo inicial é completamente randomico, o novo modelo força que os agentes com riquezas parecidas tenham mais chance de trocar riquezas. Além disso, será analisado o índice de Gini para entender quão desigual é esta sociedade e também o número de trocas que foram feitas no total entre todos os agentes do modelo.

## Hipótese causal

A hipótese causal que quero comprovar é de que quanto maior a probabilidade de troca de riqueza entre pessoas com riquezas parecidas, maior a desigualdade social e menor o número total de trocas feitas.

## Alterações no código

Adicionei duas variaveis para o modelo: uma independente a nivel do agente e uma dependente a nivel do modelo.

A primeira variavel independente é a probabilidade de troca de riqueza entre pessoas com riquezas parecidas.

A segunda variavel dependente é o número de trocas realizadas entre agentes.

## Como usar o simulador

Instale os pacotes:

- jupyter
- matplotlib
- mesa
- numpy

Execute o comando `make` para executar o simulador.

## Variáveis do CSV

As variáveis armazenadas no CSV são:

- número de agentes envolvidos no modelo
- número de trocas realizadas entre agentes
- índice de Gini
- probabilidade de troca de riqueza entre pessoas com riquezas parecidas
- número de épocas do modelo
