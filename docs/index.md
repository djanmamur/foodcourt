# Foodcourt

[![Build Status](https://travis-ci.org/djanmamur/foodcourt.svg?branch=master)](https://travis-ci.org/djanmamur/foodcourt)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Share and sell authentic food.

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

# Documentation
- [Authentication](https://djanmamur.github.io/foodcourt/api/authentication)
- [Users](https://djanmamur.github.io/foodcourt/api/users)
- [Posts](https://djanmamur.github.io/foodcourt/api/posts)

There are 3 types of users
```
ADMIN = 1
BUYER = 10
SELLER = 20
```
Notes:
##### Only admins or sellers can create a new Post
##### Only the admins or the OWNER of a Post can modify or delete Posts