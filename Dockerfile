FROM python:3.9
LABEL MAINTAINER="Daniyal Farhangi | dan.farhangi@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN python manage.py search_index --rebuild

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]