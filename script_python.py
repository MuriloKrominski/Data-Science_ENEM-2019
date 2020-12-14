"""Script para selecionar dados para análise."""
import pandas as pd

lista_arquivos = [f'parte_0{x}' for x in range(11)]

provas = ['NU_NOTA_REDACAO',
          'NU_NOTA_CN',
          'NU_NOTA_CH',
          'NU_NOTA_LC',
          'NU_NOTA_MT']

frames = []

LIMITE = 3500

for arquivo in lista_arquivos:
    file_temp = pd.read_csv(f"{arquivo}", delimiter=";", encoding="ISO-8859-1")
    file_temp = pd.DataFrame(file_temp)
    print(f'Arquivo {arquivo} criado como DataFrame')
    file_temp['NU_NOTA_FINAL'] = file_temp[provas].sum(axis=1)
    print(f'Coluna NU_NOTA_FINAL criada')
    print(f'Total de linhas e colunas: {file_temp.shape}')
    file_temp = file_temp.query('NU_NOTA_FINAL > LIMITE')
    print(f'Query do {arquivo} concluída com total de registros: {file_temp.shape} ')
    frames.append(file_temp)

print('Iniciando concatenação...')
resultado = pd.concat(frames)

print('Salvando csv...')
resultado.to_csv('data_final.csv', index=False)
print('Fim da operação')
