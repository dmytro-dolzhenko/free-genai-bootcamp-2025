FROM python:3.12-slim

COPY . /ui

WORKDIR /ui

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]