.PHONY: all
all:
	uv run hello.py

.PHONY: sync
sync:
	uv sync