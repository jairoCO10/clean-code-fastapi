FROM python:3

USER root

# Actualizar e instalar dependencias necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
    && rm -rf /var/lib/apt/lists/*




WORKDIR /usr/src/app

COPY libraries/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER root

EXPOSE 8015

CMD [ "python", "run.py" ]