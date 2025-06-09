#!/bin/bash

echo "Setting up environment variables..."
source .env

echo "Extracting data from api to target-jsonl..."
meltano run tap-adventureworks target-jsonl

echo "Import files to Databricks..."
databricks fs cp ./output/ dbfs:/Volumes/ted_dev/dev_luiz_campos/raw/api/ --recursive