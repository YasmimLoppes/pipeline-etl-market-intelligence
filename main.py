import pandas as pd
import sqlite3
import requests

# 1. EXTRAÇÃO: Buscando dados reais de mercado via API da CoinGecko
print("Iniciando Extração: Buscando dados na API...")
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
response = requests.get(url)
dados_brutos = response.json()

# 2. TRANSFORMAÇÃO: Limpeza e estruturação com Pandas
print("Iniciando Transformação: Limpando e padronizando os dados...")
df = pd.DataFrame(dados_brutos)

# Selecionamos colunas estratégicas para Inteligência de Mercado
colunas_interesse = ['symbol', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h']
df_final = df[colunas_interesse].copy()

# Data Cleaning: Tratando valores nulos para manter a integridade
df_final.fillna(0, inplace=True)

# 3. CARGA: Ingestão em banco de dados SQL (SQLite)
print("Iniciando Carga: Salvando no banco de dados SQL...")
conexao = sqlite3.connect('database_mercado.db')
df_final.to_sql('monitoramento_ativos', conexao, if_exists='replace', index=False)

print("✅ Pipeline de ETL finalizado com sucesso!")
conexao.close()
