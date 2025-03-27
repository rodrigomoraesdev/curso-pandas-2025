#%%
import pandas as pd

#%%
url='https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'

df = pd.read_html(url)
df_uf = df[1]
df_uf
# %%
df_uf.to_csv('uf.csv', index=False)

# %%
