FROM python:3.10.4-buster

RUN pip3 install fastapi uvicorn aiofiles jinja2

EXPOSE 80

COPY ./main.py /
COPY ./static /static
COPY ./templates /templates

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
