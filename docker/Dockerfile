FROM python:3.10-slim

WORKDIR /code

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

ENV PYTHONPATH="/code"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
