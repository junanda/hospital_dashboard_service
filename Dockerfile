FROM python:3.11.9-slim as base

WORKDIR /app

COPY requirement.txt ./

RUN pip install -r requirement.txt

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000" ]
