import pandas as pd
import logging
from config_logging import chamar_logging

chamar_logging()

df_compras_publicas = pd.read_csv("dados_reformulados_silver.csv")


#Tratamento Formatação
try:
    tratamento_upper = ['nome_municipio','nome_orgao','sigla_uf']
    tratamento_lower = ['orcamento_sigiloso','objeto_compra']

    #Tratando Colunas para UPPER
    for col in tratamento_upper:
        df_compras_publicas[col] = df_compras_publicas[col].str.upper().str.strip()    

    #Tratando Colunas para LOWER
    for colunas in tratamento_lower:
        df_compras_publicas[colunas] = df_compras_publicas[colunas].str.lower().str.strip()

    df_compras_publicas.columns = df_compras_publicas.columns.str.lower().str.strip()
    logging.info("Etapa Tratamento Formatação: Concluída")
except Exception as error:
    logging.exception(f"Erro na etapa Tratamento Formatação - {error}")
    raise

#Tratamento Tipo Colunas
colunas_tratamento_object = ['id_compra','sigla_uf','nome_municipio','nome_orgao','orcamento_sigiloso','objeto_compra','data_encerramento_proposta']
colunas_tratamento_int = ['ano_compra_pncp']
try:
    #Tratando Colunas Para o type OBJECT
    for coluna in colunas_tratamento_object:
        df_compras_publicas[coluna] = df_compras_publicas[coluna].astype("object")

    #Tratando Colunas Para o type Int64
    for column in colunas_tratamento_int:
        df_compras_publicas[column] = pd.to_numeric(df_compras_publicas[column])
    

    logging.info("Etapa Tratamento Tipo Colunas: Concluída")
except Exception as e:
    logging.exception(f"Erro na etapa Tratamento Tipo Colunas - {e}")
    raise

#Filtrando dados válidos e inválidos

try:
    filtro_tratamento = (
        df_compras_publicas['sigla_uf'].isnull() |
        df_compras_publicas['nome_municipio'].isnull() |
        df_compras_publicas['ano_compra_pncp'].isnull() |
        df_compras_publicas['id_compra'].isnull() |
        df_compras_publicas['nome_orgao'].isnull() |
        df_compras_publicas['objeto_compra'].isnull() 
    )

    df_compras_validos = df_compras_publicas[~filtro_tratamento]
    df_compras_invalidos = df_compras_publicas[filtro_tratamento]

    logging.info("Etapa Filtrando dados: Concluída")

except Exception as erro:
    logging.exception(f"Erro na etapa Filtrando dados - {erro}")
    raise


#
df_dados_validos = len(df_compras_validos)
df_dados_recebidos = len(df_compras_publicas)
df_dados_invalidos = len(df_compras_invalidos)
porcentagem_rejeicao = (df_dados_invalidos / df_dados_recebidos) * 100
logging.info(f"Dados Válidos: {df_dados_validos}")
logging.info(f"Dados Inválidos: {df_dados_invalidos}")
logging.info(f"Dados Recebidos: {df_dados_recebidos}")
if porcentagem_rejeicao < 10:
    logging.info(f"Porcentagem Aceitação: {porcentagem_rejeicao}")
    logging.info("Porcentagem Aceita!")
    
else:
    logging.warning("Porcentagem acima do limite!")

df_compras_validos.to_csv("dados_tratados.csv",index=False)
df_compras_invalidos.to_csv("dados_invalidos.csv",index=False)
