import pandas as pd
import logging

#Importando LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


df_compras_publicas = pd.read_csv("dados_reformulados.csv")


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
    logging.exception(f"Erro na etapa Tratamento Tipo Colunbas - {e}")

