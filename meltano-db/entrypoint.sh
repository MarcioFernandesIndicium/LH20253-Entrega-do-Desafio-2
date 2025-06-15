#!/bin/bash

echo "[$(date)] Iniciando extração do AdventureWorks..."

echo "Extraindo os dados do AdventureWorks..."
meltano run tap-mssql target-parquet || { echo "Erro na extração!"; exit 1; }

echo "Extração concluída com sucesso!"


echo "Importanto os dados extraídos para o DBFS no Databricks..."
databricks fs cp /data/extract_from_db dbfs:/Volumes/${DATABRICKS_CATALOG}/${DATABRICKS_SCHEMA}/${DATABRICKS_VOLUME_RAW}/extracted_from_db --recursive || { echo "Erro no upload para o DBFS!"; exit 1; }

echo "Dados importados com sucesso para o DBFS!"


echo "Executando o job de criação de tabelas no Databricks..."
databricks jobs run-now 532210134837132 || { echo "Erro ao executar o job de criação de tabelas!"; exit 1; }