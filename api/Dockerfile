FROM python:3.10

COPY requirements.txt .

RUN pip install --upgrade pip && pip install setuptools
RUN pip install -r requirements.txt

COPY ./src /usr/src/api

WORKDIR /usr/src/api

ENTRYPOINT [ "python", "run.py" ]
