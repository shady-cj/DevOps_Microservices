setup:
	python3 -m venv .flask-app
install:
	pip3 install --upgrade pip && pip install -r requirements.txt
lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 ./**.py
all: setup install lint

