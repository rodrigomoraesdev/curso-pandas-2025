#%%
import pandas as pd

#%%
idades = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

indexes = ['Rodrigo', 'Felipe', 'João', 'Maria', 'Ana', 'José', 'Carlos', 'Pedro', 'Paulo', 'Lucas']

series_idades = pd.Series(idades, index=indexes)

series_idades

# %%

series_idades.iloc[1]
series_idades['Felipe']
# %%
