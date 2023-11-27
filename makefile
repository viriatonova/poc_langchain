SHELL := /bin/bash
.SILENT:
.DEFAULT_GOAL := help

##### SELF-DOCUMENTATION ####

.PHONY: help
help: ## [Help}
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: dependencies
dependencies: ## [Production project dependencies]
	pip-compile -o requirements.txt pyproject.toml

.PHONY: dev_dependencies
dev_dependencies: ## [Development project dependencies]
	pip-compile -o dev-requirements.txt pyproject.toml --extra=dev

.PHONY: build
build: dev_dependencies
	source venv/bin/activate && \
	pip install -r dev-requirements.txt