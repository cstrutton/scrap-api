FROM python:3.7

RUN pip install fastapi uvicorn
RUN pip install sqlalchemy
RUN pip install python-multipart
RUN pip install pyjwt
RUN pip install passlib[bcrypt]
RUN pip install ptvsd==4.3.2

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]