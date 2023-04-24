# digikala

# About The Project
  The project is a shopping site like digikala, and it is written with new Rest Full Api architecture

## Technologies used in this project:
  - python
  - django
  - django rest framework
  - redis
  - elasticsearch
  - celery 
  - docker 
  - postgres
  - swagger
  - unit test
 


### Usage

#### Installation

* [docker](https://docs.docker.com/engine/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

**Requirements**

*Python3.9*

```
    1. Create a virtual environment via python3 -m venv venv.
    2. Activate venv through source venv/bin/activate.
    3. You must copy a sample of .env-sample in .env file with cp .env-sample .env.
    4. install all of the requirements package via command pip install -r requirements.txt.
    5. Run the following command to get the database ready to go:

        python manage.py migrate
```

*Now you can run the project with **python manage.py runserver** and this site will be available on localhost://8000*