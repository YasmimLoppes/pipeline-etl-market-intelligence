import pandas as pd
import sqlite3
import requests
import sys

def executar_pipeline():
    print("🚀 Iniciando Pipeline de ETL...")

    # 1. EXTRAÇÃO com Tratamento de Erros
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Verifica se a API respondeu com sucesso (Erro 200)
        dados_brutos = response.json()
        print("✅ Dados extraídos com sucesso via API.")
    except Exception as e:
        print(f"❌ Erro na extração: {e}")
        sys.exit() # Para o código se não houver dados

    # 2. TRANSFORMAÇÃO (Lógica de Negócio)
    df = pd.DataFrame(dados_brutos)
    colunas_interesse = ['symbol', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h']
    df_final = df[colunas_interesse].copy()
    
    # Tratamento básico: preenche valores nulos com zero para evitar quebra no SQL
    df_final.fillna(0, inplace=True)
    print("✅ Transformação e limpeza concluídas.")

    # 3. CARGA (Persistência em SQL)
    try:
        conexao = sqlite3.connect('database_mercado.db')
        df_final.to_sql('monitoramento_ativos', conexao, if_exists='replace', index=False)
        conexao.close()
        print("✅ Carga no banco de dados SQL finalizada com sucesso!")
        print("🏁 Pipeline concluído sem erros.")
    except Exception as e:
        print(f"❌ Erro ao salvar no banco: {e}")

if __name__ == "__main__":
    executar_pipeline()
