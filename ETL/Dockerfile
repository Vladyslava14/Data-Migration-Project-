FROM python:3.11-slim

WORKDIR /app

COPY . /app/ETL

ENV PYTHONPATH="/app"

RUN pip install --no-cache-dir -r /app/ETL/requirements.txt

CMD ["python", "/app/ETL/etl_pipeline.py"]
