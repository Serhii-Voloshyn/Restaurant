# Restaurant
Back end for managing lunch places.

## Installation

### Clone or Download

-  Clone this repo to your local machine using   
```
git clone https://github.com/Serhii-Voloshyn/Restaurant.git
```

### Required to install

- Project reqirements:
```
pip install -r /requirements.txt
```

### Environment

- Add the environment variables file (.env) to the project folder.
It must contain the following settings:
```
SECRET_KEY = 'YOUR_SECRET_KEY'
DEBUG = False
DB_NAME='YOUR_DB_NAME'
DB_USER='YOUR_DB_USER'
DB_PASS='YOUR_DB_PASSWORD'
DB_HOST='YOUR_DB_HOST'
```

### How to run locally

- Start the terminal.
- Go to the directory "your way to the project" / restaurant / restaurant
- Run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### How to run Docker

- Run our project using Docker:
```
docker-compose up --build
```



### Setup

- Create a superuser using the terminal:    
```
python manage.py createsuperuser
```

----

## Tests

- Run project tests:
```
pytest
```
