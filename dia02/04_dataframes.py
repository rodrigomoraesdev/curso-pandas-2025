#%%
#Importação da biblioteca pandas
import pandas as pd

# %%
#Criando DataFrame de Clientes
df_clientes = pd.read_csv('../data/clientes.csv')
df_clientes.head(2)
df_clientes.tail(3)

# %%
#Shape do DataFrame
df_clientes.shape

# %%
#Nomes das colunas
df_clientes.columns

# %%
#Index do DataFrame
df_clientes.index
# %%
#informações do DataFrame
df_clientes.info(memory_usage='deep')
# %%
#DTypes do DataFrame
df_clientes.dtypes['flEmail']
#%%
