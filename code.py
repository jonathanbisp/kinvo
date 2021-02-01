# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:28:59 2021

@author: Jonathan Bispo
"""

import pandas as pd

df = pd.read_csv('bank.csv', sep=";")

# Checando integridade dos dados
df.isnull().sum()

# Resultados interessantes, a maior parte da população tem entre 30 e 50 anos. Uma distribuição bem normal
df['age'].describe()
df.boxplot(column=['age'])

# Pergunta, em quanto tempo em média uma pessoa opta por pegar um empréstimo?
duration = df.loc[lambda pessoa: pessoa.y == "yes", ['duration']]
durationMean = duration.mean()
duration.hist()

# Pergunta, é mais fácil pessoas casadas ou solteiras pegarem um empréstimo?
casadas = df.loc[lambda pessoa: pessoa.marital == "married"]
casadasEmprestimoPositivo = len(casadas.loc[lambda pessoa: pessoa.y == "yes"])

solteiras = df.loc[lambda pessoa: pessoa.marital == "single"]
solteirasEmprestimoPositivo = len(solteiras.loc[lambda pessoa: pessoa.y == "yes"])

# Nessa amostra, de 4521 pessoas. 2797 eram casadas e 1196 eram solteiras. 
# 277 das pessoas casadas conseguiram o empréstimo e 167 solteiras conseguiram
# Neste momento, podemos parar e pensar que é mais fácil uma pessoa casada conseguir... Mas na verdade
# Ocorre que há uma disparidade na quantidade de elementos casados e solteiros... Daí temos que fazer
# Uma matemática básica, dividir a quantidade de elementos da maior população pela menor, para obter
# O multiplicador entre eles. E daí multiplicar esse valor pelo menor... Para obter um resultado mais concreto

totalCasadas = len(casadas)
totalSolteiras = len(solteiras)

multiplicadorPopulacao = totalCasadas/totalSolteiras

solteirasEmprestimoPositivo *= multiplicadorPopulacao

# Portanto, para um mesmo tamanho de população através da análise desses dados
# Chego a conclusão de que é mais fácil uma pessoa solteira conseguir.