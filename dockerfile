FROM python:3.11.3

WORKDIR /app

COPY  PrubaTecnica/ .

RUN pip install -r requirements.txt

RUN python populate_db.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]