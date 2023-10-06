# %% [markdown]
# # **Distribuição Discreta**

# %%
import numpy as np
import pandas as pd

# %%
enem_sp = pd.read_csv('./datasets/enem_2019_tratado.csv',
                      sep=',', encoding='iso-8859-1')

# %% [markdown]
# ## Distribuição Binomial

# %%
from scipy.stats import binom  

# %%
# PROBABILIDADE DE RETIRAR UMA MULHER
mulher_enem = enem_sp.loc[enem_sp.SEXO == 'F']

# %%
p = len(mulher_enem) / len(enem_sp)
p

# %% [markdown]
# binom.pmf = valor pontual
# 
# binom.cdf = faixa de valores (acumulada)

# %%
# PROBABILIDADE DE RETIRAR EXATAMENTE 4 MULHERES NUM TOTAL DE 10 AMOSTRAS

binom.pmf(4,10,p)

# Primeiro parâmetro:valor ou limite que se está pretendo calcular
# Segundo: número de tentativas
# Terceiro: probabilidade de um sucesso.

# %%
# PROBABILIDADE DE RETIRAR PELO MENOS UMA MULHER NUM TOTAL DE 10 AMOSTRAS

p0 = 1 - binom.pmf(0,10,p)
p0

# %%
# PROBABILIDADE DE RETIRAR MAIS DO QUE 1 MULHER NUM TOTAL DE 10 AMOSTRAS
p1 = 1 - (binom.pmf(0,10,p)+binom.pmf(1,10,p))
p1

# %%
# PROBABILIDADE DE RETIRAR MAIS DO QUE 3 MULHERES NUM TOTAL DE 10 AMOSTRAS

p2p2 = 1 - (binom.pmf(0,10,p)+binom.pmf(1,10,p)+binom.pmf(2,10,p)+binom.pmf(3,10,p))

# %%
p2 = binom.pmf(4,10,p)+binom.pmf(5,10,p)+binom.pmf(6,10,p)+binom.pmf(7,10,p)+binom.pmf(8,10,p)+binom.pmf(9,10,p)+binom.pmf(10,10,p)
p2

# %%
# OUTRA FORMA
p3 = 1 - binom.cdf(3, 10, p)
p3

# %%
# PROBABILIDADE DE RETIRAR MAIS DO QUE 8 MULHERES NUM TOTAL DE 10 AMOSTRAS
p4 = binom.pmf(9,10,p)+binom.pmf(10,10,p)
p4


# %%
# OUTRA FORMA
p5 = binom.cdf(10, 10, p) - binom.cdf(8, 10, p)
p5

# %% [markdown]
# ## Distribuição Geométrica

# %%
from scipy.stats import geom

# %%
# PROBABILIDADE DE RETIRAR 3 AMOSTRAS E NENHUMA SER MULHER
# geom.pmf(x,p) x representa a tentativa que se obteve sucesso e p a probabilidade
geom.pmf(4, p) 



# %% [markdown]
# ## Distribuição de Poisson

# %%
from scipy.stats import poisson

# %%
# Num local de prova, 100 vestibulandos, normalmente, terminaram a prova em 2 horas (tempo mínimo).
# Probabilidade de exatamente 90 vestibulandos terminarem a prova em 2h.

# poisson.pmf(x, m) x é a quantidade de ocorrências EM ESTUDO e m é a taxa de ocorrências.

poisson.pmf(90,100)


