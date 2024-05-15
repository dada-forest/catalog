SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: build shell chown dev_server dcu dcs fmt


build:
	docker build -f Dockerfile -t catalog:latest .

shell:
	docker exec -it catalog bash

chown:
	sudo chown $(USER):$(USER) -R .

dcu:
	docker compose -f compose.yml up -d --build
	# docker run --rm -it -p 8000:8000 -v $(PWD):/catalog catalog:latest fastapi dev main.py --host 0.0.0.0 --reload

dcs:
	docker compose -f compose.yml stop

fmt:
	docker run -v $(PWD):/catalog -it catalog:latest ruff format .

# dcu:
# 	docker compose -f compose.yml up -d --build
