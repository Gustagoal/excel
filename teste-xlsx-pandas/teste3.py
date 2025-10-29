import pandas as pd 

tabela = pd.read_excel("vendas.xlsx")
tabela = tabela.dropna() # remove os valores vazios


