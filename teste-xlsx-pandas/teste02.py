import pandas as pd 

df1 = pd.read_excel(r"teste-xlsx-pandas/categorias.xlsx")
df2 = pd.read_excel(r"teste-xlsx-pandas/produtos.xlsx")

planilha_unica = pd.merge(df1,df2,how="inner",on="ID_Categoria") # Fazendo o procv
planilha_unica.to_excel("vendas.xlsx") # Salvando em excel



analise = pd.read_excel("vendas.xlsx")
print(analise[["Categoria","Preco_Unit"]].describe())
