import pandas as pd
import glob
import os

arquivos = glob.glob("../../dados/demonstracoes_contabeis/*.csv")

dfs = []

for arquivo in arquivos:
    nome_arquivo = os.path.basename(arquivo).replace('.csv', '')
    trimestre, ano = nome_arquivo[:2], nome_arquivo[2:]

    df = pd.read_csv(arquivo, delimiter=';', encoding='utf-8', decimal=',')
    df['trimestre'] = trimestre
    df['ano'] = int(ano)

    df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True, errors='coerce')

    dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

df_final.to_csv("../../dados/demonstracoes_contabeis/demonstracoes_contabeis_completo.csv", sep=';', encoding='utf-8', index=False, decimal='.')
