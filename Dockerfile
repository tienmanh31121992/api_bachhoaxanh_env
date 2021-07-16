FROM python:3.8
WORKDIR /my-api
COPY ./ ./
RUN pip3 install -r requirements.txt
CMD python run.py
