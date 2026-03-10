# pipeline-etl-market-intelligence

⚙️ Fluxo de integração de dados de inteligência de mercado, explorando arquitetura de dados e automação de APIs.

# 🚀 Pipeline de ETL: Inteligência de Mercado (Data Intelligence)

Este projeto demonstra a construção de um pipeline de dados automatizado utilizando **Python** e **SQL**, focado em coletar, tratar e estruturar informações estratégicas para suporte à tomada de decisão.

## 📝 Descrição do Projeto
O objetivo principal é simular um fluxo real de **Engenharia de Dados**: extrair dados brutos de uma API de mercado, realizar o processo de **Data Cleaning** (Limpeza e Padronização) e carregar as informações tratadas em um banco de dados relacional. Este fluxo é essencial para empresas que trabalham com Big Data e análise preditiva, como a **Data Stone**.

## 🛠️ Tecnologias e Ferramentas
* **Python 3.x:** Linguagem base para o script de automação.
* **Pandas:** Biblioteca líder para manipulação e limpeza de DataFrames.
* **Requests:** Utilizada para o consumo de APIs REST e extração de dados brutos.
* **SQLite3:** Banco de dados relacional utilizado para o armazenamento estruturado (Carga).

## ⚙️ Arquitetura do Pipeline (Processo ETL)
1.  **Extract (Extração):** Coleta automatizada dos 10 principais ativos de mercado via API pública.
2.  **Transform (Transformação):** * Seleção de colunas estratégicas (KPIs de preço e market cap).
    * Tratamento de valores ausentes (Missing Values) para garantir a integridade.
    * Padronização dos dados para consumo em ferramentas de BI.
3.  **Load (Carga):** Ingestão dos dados limpos em tabelas SQL preparadas para consultas analíticas.

## 📈 Valor para o Negócio
Este projeto elimina a necessidade de coleta manual de dados, garantindo que a equipe de inteligência de mercado tenha acesso a dados **confiáveis, limpos e centralizados**, permitindo uma análise mais ágil das tendências do setor.

---
**Desenvolvido por Yasmin Lopes** | Estudante de Análise e Desenvolvimento de Sistemas (3º Semestre)

