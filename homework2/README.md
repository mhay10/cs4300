# CS4300 - Homework 2

This folder contains Homework 2 for CS4300.  
The deployed application can be found on [Render](https://cs4300-j3t3.onrender.com).

## Installation

1. Navigate to the root directory of this project.

    ```bash
    cd cs4300/homework2
    ```

2. Create a virtual environment and activate it

    ```bash
    python3 -m venv venv --system-site-packages
    source venv/bin/activate
    ```

3. Install the required dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Running the Web Application 

From the `homework2` directory, run the following command to start the web application:

```bash
python manage.py runserver 0.0.0.0:3000
```

## Populating the Database

There is a script included in the `bookings` app that can be used to populate the database with test data. To run the script, run the following command:

```bash
python manage.py populate_test_data
```

## Testing the Web Application

To run the tests, run the following command:

```bash
python manage.py test
```

## AI Usage in Development

I used Claude alot throughout the development of this project as I am brand new to Django. I asked for a beginners guide to building the web application based on the PDF provided and Claude provided code examples for models, views, serializers, and templates. I used the provided code as a starting point and made changes as changing the seat availability status and custom HTML templates. 

I also asked Claude to help me with what tests to write for the API and HTML views and how to write a Django test case. When I was writing tests for the API, I ran into a CSRF 403 error when trying to book a movie seat. I asked Claude for help with this and it helped me add the trusted domains to the settings file.

