import pandas as pd
import logging
from config_logging import chamar_logging
#Chamando Logging
chamar_logging()

logging.info("Iniciando Pipeline...")

#Lendo CSV
try:
    df_compras = pd.read_csv("compras_publicas.csv", dtype=str)
    df_compras = df_compras[['id_compra','sigla_uf','nome_municipio','ano_compra_pncp','nome_orgao','orcamento_sigiloso','objeto_compra','valor_total_estimado','data_encerramento_proposta']]

    #Transformando DATASET novo em CSV
    df_compras.to_csv("dados_reformulados.csv",index=False)
    logging.info("Etapa Extração: Concluída")

except Exception as e:
    logging.exception(f"Erro na ETAPA: Extração - {e}")
    raise




