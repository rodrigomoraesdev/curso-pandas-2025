#%%
import pandas as pd
# %%
df = pd.read_csv('../data/clientes.csv')
df
# %%
df.to_csv('../data/clientes2.csv', index=False)
# %%

df.to_parquet('../data/clientes.parquet', index=False)

# %%
df2 = pd.read_parquet('../data/clientes.parquet')
df2
# %%
df.to_excel('../data/clientes.xlsx', index=False)
# %%
df3 = pd.read_csv('../data/exemplo.csv', sep=';')
df3
# %%
df3.to_csv('../data/exemplo2.csv', sep='?')

# %%
