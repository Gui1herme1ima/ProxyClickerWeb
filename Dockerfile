FROM python:3.12-slim

# Instale dependências
RUN apt-get update && apt-get install -y zstd

# Copie o projeto
COPY . /app
WORKDIR /app

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Comando para rodar a aplicação
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
