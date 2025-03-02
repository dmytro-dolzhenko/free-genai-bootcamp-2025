FROM python:3.12-slim

COPY . /megaservice

WORKDIR /megaservice

RUN pip install -r requirements.txt

CMD ["python", "megaservice.py"]