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

    # Padroniza a data no formato ISO aceito pelo PostgreSQL
    df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True, errors='coerce')
    df['DATA'] = df['DATA'].dt.strftime('%Y-%m-%d')

    # Renomeia colunas para letras minúsculas e sem espaços
    df.columns = df.columns.str.lower().str.strip()

    dfs.append(df)

# Junta tudo
df_final = pd.concat(dfs, ignore_index=True)

# Troca NaN por None
df_final = df_final.where(pd.notnull(df_final), None)

# Exporta para CSV final
df_final.to_csv(
    "../../dados/demonstracoes_contabeis/demonstracoes_contabeis_completo.csv",
    sep=';',
    encoding='utf-8',
    index=False,
    decimal='.'
)
