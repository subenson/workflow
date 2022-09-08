setup:
	python3 -m venv ~/.workflow
	
install:
	pip install --upgrade pip && pip install -r requirements.txt
	
test:
	python -m pytest tests/*.py
	
all: install test