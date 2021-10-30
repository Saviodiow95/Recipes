# Recipes

[![Python Version](https://img.shields.io/badge/python-9.3.0-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.8-brightgreen.svg)](https://djangoproject.com)



##[Documentation](documentation.md)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/Saviodiow95/Recipes
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.