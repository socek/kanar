FROM python:3.6
RUN mkdir -p /code

WORKDIR /code

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

COPY code/setup.py .
RUN python setup.py develop
