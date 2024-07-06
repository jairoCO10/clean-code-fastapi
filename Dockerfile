FROM python:3

WORKDIR /usr/src/app

COPY libraries/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8015

CMD [ "python", "run.py" ]