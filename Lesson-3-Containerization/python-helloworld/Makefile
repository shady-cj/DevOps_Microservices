setup:
	python -m venv ~/.flask-app
install:
	pip install --upgrade pip && pip install -r requirements.txt
lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 ./**.py
all: setup install lint

