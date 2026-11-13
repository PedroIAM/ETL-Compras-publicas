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

    #Tratando Colunas para UPPER
    for col in tratamento_upper:
        df_compras_publicas[col] = df_compras_publicas[col].str.upper().str.strip()    

    df_compras_publicas.columns = df_compras_publicas.columns.str.lower().str.strip()
    df_compras_publicas['orcamento_sigiloso'] = df_compras_publicas['orcamento_sigiloso'].str.lower().str.strip()
    df_compras_publicas['objeto_compra'] = df_compras_publicas['objeto_compra'].str.lower().str.strip()
    logging.info("Etapa Tratamento Formatação: Concluída")
except Exception as error:
    logging.exception(f"Erro na etapa Tratamento Formatação - {error}")
    raise

#Tratamento Tipo Colunas
colunas_tratamento = ['id_compra','sigla_uf','nome_municipio','nome_orgao','orcamento_sigiloso','objeto_compra','data_encerramento_proposta']
try:
    for coluna in colunas_tratamento:
        df_compras_publicas[coluna] = df_compras_publicas[coluna].astype("object")

print(df_compras_publicas.info())
print(df_compras_publicas.head(5))
print("teste atualizandooo..")