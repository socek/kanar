FROM python:3.6
RUN mkdir -p /code

WORKDIR /code
COPY code/setup.py .
COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt
RUN python setup.py develop
