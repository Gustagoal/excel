import pandas as pd 

tabela = pd.read_excel("produtos.xlsx")
tabela = tabela.dropna() # remove os valores vazios

print(tabela)
