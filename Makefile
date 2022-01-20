PROJECT_NAME=KNOW_YOUR_MEME_BOT

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

develop: ## Runs the discord-bot locally
	python3 ./discord-bot.py

runtime: ## Creates container from Dockerfile
	docker build . -t knowyourmeme-bot:runtime
