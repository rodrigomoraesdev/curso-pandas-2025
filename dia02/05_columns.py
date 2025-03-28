#%%
import pandas as pd
# %%
df = pd.read_csv('../data/transacoes.csv')
df.head()
# %%
df.shape
# %%
df.columns
# %%
df.index
# %%
df.info()
# %%
df.dtypes
# %%
df.rename(columns={'qtdePontos': 'qtPontos', 'descSistemaOrigem': 'SistemaOrigem'}, inplace=True)
# %%
df
# %%
df[['idCliente', 'SistemaOrigem']]

# %%
#SELECT * FROM DF
df
# %%
df[['idCliente', 'SistemaOrigem']].sample(10)
# %%

df[['idCliente', 'idTransacao', 'idTransacao']].head()
# %%
colunas = list(df.columns)
colunas.sort()
colunas
# %%
df = df[colunas]
# %%
df
# %%
