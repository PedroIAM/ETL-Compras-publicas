import pandas as pd
import logging

#Importando LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


df_compras_publicas = pd.read_csv("dados_reformulados.csv")


#Tratamento Formatação
df_compras_publicas.columns = df_compras_publicas.columns.str.lower().str.strip()
df_compras_publicas['sigla_uf'] = df_compras_publicas['sigla_uf'].str.upper().str.strip()
df_compras_publicas['nome_municipio'] = df_compras_publicas['nome_municipio'].str.upper().str.strip()
df_compras_publicas['nome_orgao'] = df_compras_publicas['nome_orgao'].str.upper().str.strip()
df_compras_publicas['orcamento_sigiloso'] = df_compras_publicas['orcamento_sigiloso'].str.lower().str.strip()
df_compras_publicas['objeto_compra'] = df_compras_publicas['objeto_compra'].str.lower().str.strip()

#Tratamento Tipo Colunas
df_compras_publicas['ano_compra_pncp'] = pd.to_numeric(df_compras_publicas['ano_compra_pncp'])

print(df_compras_publicas.info())
print(df_compras_publicas.head(5))
print("teste")