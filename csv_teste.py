import pandas as pd

# Carregando o arquivo CSV
data = pd.read_csv(r"C:\Users\wallingson.silva\Downloads\C170.csv")

# Obtendo os valores únicos da coluna 'cnpj_empresa'
valores_cnpj = data['cnpj_empresa'].unique()

# Dividindo o arquivo com base nos valores únicos da coluna 'cnpj_empresa'
for cnpj in valores_cnpj:
    # Criando um novo DataFrame para cada valor único de 'cnpj_empresa'
    novo_dataframe = data[data['cnpj_empresa'] == cnpj]

    # Salvando o novo DataFrame em um arquivo CSV com o nome do CNPJ
    novo_dataframe.to_csv(f'{cnpj}.csv', index=False)
