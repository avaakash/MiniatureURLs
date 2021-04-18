# MiniatureURLs
MiniatureURLs is a URL shortening service built using Django. 

*Website*: [miniatureurls.ml](miniatureurls.ml)
Create an account and then start using the service. The front-end is basic, will be improved with time.


## Live Features
Currently there are a few features supported only

 - Shortening URL
 - Setting custom expiry time
 - Editing redirection URL
 - Visits counter
 - Account Authentication

## Upcoming Features
With time, new features will be added, currently these are in the planning

 1. Custom shortened URLs

# Run Locally
If you wish to run the service locally, follow these steps to setup a django server and run the service on localhost. *It's pretty easy*

#### Step 1:
Clone the repository and change your directory to the project directory
#### Step 2:
Install the requirements using *pip*. 

    pip install -r requirements.txt
This will install all the requirements automatically.
#### Step 3:
Next we will have to setup our database, we will be running SQLite3 for development, as it's very to setup. Just follow these commands and you are good to go!

    python manage.py migrate
This will create all the required tables in the database.
#### Step 4:
Now it's time to run the server.

    python manage.py runserver
#### Step 5:
Access the service by going to **localhost:8000**

That's it, we are done.

### Extras
If you wish to create a superuser account, we can do that using the terminal.

    python manage.py createsuper
The admin panel is available at **localhost:8000/admin**
