FROM python:3.6
RUN mkdir -p /code
RUN mkdir -p /project.egg-info

WORKDIR /code
RUN ln -s /project.egg-info rotarran.egg-info

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

COPY code/setup.py .
RUN python setup.py develop
