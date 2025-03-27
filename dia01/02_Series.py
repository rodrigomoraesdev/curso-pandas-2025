#%%
import pandas as pd

#%%

idades = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

series_idades = pd.Series(idades)
series_idades.head()

series_idades.describe()

series_idades.mean()

series_idades.var()

# %%
