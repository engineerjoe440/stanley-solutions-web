FROM python:3.7

RUN pip install fastapi uvicorn aiofiles

EXPOSE 80

COPY ./main.py /app/
COPY ./static /app/static

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
