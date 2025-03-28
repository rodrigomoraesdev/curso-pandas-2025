#%%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %%

pontos = [10, 1, 2, 50, 100, 88, 99]

valores_maior = []

for i in pontos:
    if i >= 50:
        valores_maior.append(i)

valores_maior
# %%
valores_maiores = [i for i in pontos if i >=50]
valores_maiores
# %%
import pandas as pd

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo['nome'] == 'teo'
brinquedo[filtro]


# %%

df = pd.read_csv('../data/transacoes.csv')
df.head()

# %%

filtro = (df['qtdePontos'] >= 50) & (df['qtdePontos'] < 100)
df[filtro]
# %%

filtro = (df['qtdePontos'] == 1) | (df['qtdePontos'] > 100)
df[filtro]

# %%
filtro = (df['qtdePontos'] > 0) & (df['qtdePontos'] <= 50) | (df['dtCriacao'] >= '2025-01-01')
df[filtro]
# %%
