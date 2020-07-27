import pandas as pd

df_raw = pd.read_csv('receitas.csv', sep='";"')

#df_raw.head()

#for x in df_raw.columns: 
 #   print(x)

df = df_raw.rename(columns={'"CÓDIGO ÓRGÃO SUPERIOR;""NOME ÓRGÃO SUPERIOR"':'Cod_orgao_superior;Nome_orgao_superior',
                                 '"CÓDIGO ÓRGÃO"':'Codigo_orgao',
                                 '"NOME ÓRGÃO"':'Nome_orgao',
                                 '"CÓDIGO UNIDADE GESTORA"':'Cod_unid_gestora',
                                 '"NOME UNIDADE GESTORA"':'Nome_unid_gestora',
                                 '"CATEGORIA ECONÔMICA"':'Categoria_eco',
                                 '"ORIGEM RECEITA"':'Origem_receita',
                                 '"ESPÉCIE RECEITA"':'Especie_receita',
                                '"DETALHAMENTO"':'Detalhamento',
                                '"VALOR PREVISTO ATUALIZADO"':'Valor_previsto_atualiz',
                                '"VALOR LANÇADO"':'Valor_lancado',
                                '"VALOR REALIZADO"':'Valor_realizado',
                                '"PERCENTUAL REALIZADO"':'Percentual_realizado',
                                '"DATA LANÇAMENTO"':'Data_lancamento',
                                '"ANO EXERCÍCIO""",,,,,,,,,':'Ano_exercicio'})   

df = df.replace({'"':''}, regex=True)
df = df.replace({',,,,,':''}, regex=True)
df = df.replace({',,,,':''}, regex=True)
df = df.replace({',,,':''}, regex=True)
df = df.replace({',,':''}, regex=True)
df = df.replace({',':'.'}, regex=True)

df['Ano_exercicio'] = df['Ano_exercicio'].replace({'2019.':'2019'}, regex=True)


df['Cod_orgao_superior'], df['Nome_orgao_superior'] = df['Cod_orgao_superior;Nome_orgao_superior'].str.split(';', 1).str
del df['Cod_orgao_superior;Nome_orgao_superior']

cols = df.columns.tolist()
cols = cols = cols[-2:] + cols[:-2]
df = df[cols]

#df.head(100)

#df.describe(include='object')
#df.dtypes

df['Valor_previsto_atualiz'] = df['Valor_previsto_atualiz'].astype(float)
df['Valor_lancado'] = df['Valor_lancado'].astype(float)
df['Valor_realizado'] = df['Valor_realizado'].astype(float)
df['Percentual_realizado'] = df['Percentual_realizado'].astype(float)
df['Valor_realizado'] = df['Valor_realizado'].astype(float)
df['Ano_exercicio'] = df['Ano_exercicio'].astype(int)
df['Data_lancamento'] = df['Data_lancamento'].astype('datetime64[ns]')

#Missingno é usado para checar por valores vazios e mostrar sua posic no dataset
#conda install -c conda-forge missingno
#import missingno as msno
#msno.matrix(df)

df.to_csv('receitas_final2.csv')