FROM python:3.12-slim

RUN adduser joel

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=joel:joel . .

USER joel

EXPOSE 5001

CMD ["python", "app.py"]                         
