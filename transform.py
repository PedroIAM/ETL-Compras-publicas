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
    df_compras_publicas.columns = df_compras_publicas.columns.str.lower().str.strip()
    df_compras_publicas['sigla_uf'] = df_compras_publicas['sigla_uf'].str.upper().str.strip()
    df_compras_publicas['nome_municipio'] = df_compras_publicas['nome_municipio'].str.upper().str.strip()
    df_compras_publicas['nome_orgao'] = df_compras_publicas['nome_orgao'].str.upper().str.strip()
    df_compras_publicas['orcamento_sigiloso'] = df_compras_publicas['orcamento_sigiloso'].str.lower().str.strip()
    df_compras_publicas['objeto_compra'] = df_compras_publicas['objeto_compra'].str.lower().str.strip()
    logging.info("Etapa Tratamento Formatação: Concluída")
except Exception as error:
    logging.exception(f"Erro na etapa Tratamento Formatação - {error}")
    raise



print(df_compras_publicas.info())
print(df_compras_publicas.head(5))
print("teste atualizandooo..")