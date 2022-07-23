setup:
	python3 -m venv .flask-app && source .flask-app/bin/activate
install:
	pip3 install --upgrade pip && pip install -r requirements.txt
lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203 ./**.py
all: setup install lint

