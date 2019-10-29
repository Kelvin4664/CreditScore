# CreditScore

Just for demonstration purpose,
Credit Score app that allows lenders to get the credit score of a someone looking to get a loan and a report stating whether it's low or high.

# installation instriction
- clone this repo
- create a new virtual environment and
- pip install -r requirements.txt

This project assumes that all credit details are saved to our DB
it can likewise be modified to be retrieved from an API if the credit details are in an external resource

# Running the project
-  run manage.py migrate
-  run manage.py create superuser and supply the required fields(to use authentication)
-  finally, manage.py runserver to start the development server.

To authenticate, use the admin site: localhost:8000/admin
Add a few users
Create loans and assign to users,

Test the API at localhost:8000/score/*username*
