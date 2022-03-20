FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /AerLabs
COPY . /AerLabs/
RUN pip install -r requirements.txt

