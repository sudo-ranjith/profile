FROM python:3.8

WORKDIR /run
COPY ..

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["run.py"]
