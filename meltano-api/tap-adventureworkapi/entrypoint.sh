#!/bin/bash

echo "[$(date)] Iniciando extração do AdventureWorks..."

echo "Extraindo os dados do AdventureWorks..."
meltano run tap-adventureworkapi target-jsonl || { echo "Erro na extração!"; exit 1; }

echo "Extração concluída com sucesso!"

echo "Import files to Databricks..."
databricks fs cp /data/extract_from_api dbfs:/Volumes/ted_dev/dev_marcio_fernandes/raw --recursive