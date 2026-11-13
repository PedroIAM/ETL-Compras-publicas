from sqlalchemy import create_engine,text
import pandas as pd
import logging
from config_logging import chamar_logging
import os
from dotenv import load_dotenv

load_dotenv()

#Chamando LOGGING
chamar_logging()

#Criando getenv
usuario = os.getenv("usuario")
senha = os.getenv("senha")
porta = os.getenv("port")
host = os.getenv("host")
data_base = os.getenv("data_base")

#Criando Conexão SQLAlchemy
engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{data_base}")

#Preparando dados para subir
df_dados_limpos = pd.read_csv("dados_tratados.csv")
registros = df_dados_limpos.to_dict(orient='records')

def subindo_dados_validos():
        with engine.begin() as conect:
         conect.execute(text(
            """INSERT INTO compras_publicas_valido(
        id_compra,
        sigla_uf,
        nome_municipio,
        ano_compra_pncp,
        nome_orgao,
        orcamento_sigiloso,
        objeto_compra,
        valor_total_estimado,
        data_encerramento_proposta
        ) VALUES (
        :id_compra,
        :sigla_uf,
        :nome_municipio,
        :ano_compra_pncp,
        :nome_orgao,
        :orcamento_sigiloso,
        :objeto_compra,
        :valor_total_estimado,
        :data_encerramento_proposta
        )
        """
        ),
        registros)
         
def definindo_etapas(nome,funcao):
     logging.info(f"Iniciando Etapa: {nome}")
     try:
          resultado = funcao()
          logging.info(f"Etapa {nome}: Concluída")
          return resultado
     except Exception as error:
          logging.exception(f"Erro na etapa {nome} - {error}")
          raise

chamando_funcao_subir_validos = definindo_etapas("Subindo dados válidos",subindo_dados_validos)
chamando_funcao_subir_validos