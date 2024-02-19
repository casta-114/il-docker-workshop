from python:3-slim

workdir /app

copy /src .
run pip install -r requirements.txt

entrypoint ["python", "main.py"]
