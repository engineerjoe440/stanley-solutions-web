FROM python:3.9

RUN pip install fastapi uvicorn aiofiles

EXPOSE 80

COPY ./main.py /
COPY ./static /static
COPY ./templates /templates

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
