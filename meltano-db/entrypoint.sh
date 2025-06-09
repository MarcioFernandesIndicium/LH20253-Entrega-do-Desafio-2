#!/bin/bash

echo "[$(date)] Iniciando extração do AdventureWorks..."

echo "Extraindo os dados do AdventureWorks..."
meltano run tap-mssql target-jsonl || { echo "Erro na extração!"; exit 1; }

echo "Extração concluída com sucesso!"

# echo "Import files to Databricks..."
# databricks fs cp ./output/ dbfs:/Volumes/ted_dev/dev_luiz_campos/raw/api/ --recursive