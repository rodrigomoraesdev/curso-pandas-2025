#%%
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv')
df.head()

# %%
filtro = (df['idProduto'] == 5) | (df['idProduto'] ==11)
df[filtro]
# %%

filtro = [5,11]
df[df['idProduto'].isin(filtro)]

# %%

clientes = pd.read_csv('../data/clientes.csv')
clientes
# %%

clientes[clientes['dtCriacao'].notna()]

# %%
clientes[clientes['dtCriacao'].isna()]
# %%
