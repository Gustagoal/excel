import pandas as pd


p1 = pd.read_excel("teste-xlsx-pandas\categorias.xlsx")
p2 = pd.read_excel("teste-xlsx-pandas\produtos.xlsx")

juntar = pd.merge(p1,p2,how='inner',on="ID_Categoria")

juntar.to_excel("planilha_unificada.xlsx")