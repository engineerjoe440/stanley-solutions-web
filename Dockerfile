FROM python:3.7

RUN pip install fastapi uvicorn aiofiles

EXPOSE 80

COPY ./main.py /
COPY ./static /static

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
