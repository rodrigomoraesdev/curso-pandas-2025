#%%
import pandas as pd

#%%
idades = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

nomes = ['Rodrigo', 'Felipe', 'João', 'Maria', 'Ana', 'José', 'Carlos', 'Pedro', 'Paulo', 'Lucas']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df['Idades'] = series_idades
df['Nomes'] = nomes
df
# %%

df['Nomes']
df.loc[0]['Nomes']
# %%
df.iloc[-1]['Idades']
# %%
