# Variáveis
VENV=.venv
ACTIVATE=source $(VENV)/bin/activate
MELTANO=meltano

.PHONY: help setup install extract

help:
	@echo "Comandos:"
	@echo "  make setup      - Cria e ativa venv, instala meltano e dependências"
	@echo "  make extract    - Roda extração com meltano (tap + target)"
	@echo "  make install    - Instala seu projeto local (pip install -e .)"

setup:
	python3 -m venv $(VENV)
	$(ACTIVATE) && pip install --upgrade pip
	$(ACTIVATE) && pip install meltano

install:
	$(ACTIVATE) && pip install -e .

extract:
	$(ACTIVATE) && export $$(cat .env | xargs) && $(MELTANO) run tap-adventureworkapi target-jsonl

