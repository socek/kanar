FROM python:3.6
RUN mkdir -p /code

WORKDIR /code
COPY code/setup.py .
COPY requirements_dev.txt .
RUN pip3 install -r requirements_dev.txt
RUN python3 setup.py develop
