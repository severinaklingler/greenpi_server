# greenpi_server
Server for GreenPi

To install the server 

Download [Heroku](https://heroku.com) for your system.

```pipenv install
   pipenv shell
   heroku create
   git push heroku master
   heroku run python manage.py migrate
   heroku ps:scale web=1
   heroku open
```


To run the app locally (first line only the first time)
```
   python manage.py collectstatic
   python manage.py migrate
   heroku local web -f Procfile.windows
```

If you add a model you have to call
```
   python.exe .\manage.py makemigrations
```


# Create a user and receive an auth token for the api
First create a user and the receive the auth token.
```
   python manage.py createsuperuser --email test@example.com --username test 
   curl.exe --data "username=test&password=pw" http://127.0.0.1:5000/api-token-auth/
``` 


# Add measurements
curl.exe -X POST http://127.0.0.1:5000/add_measurement/ -H 'Authorization: Token 658e9405f5681018e101c3ceba43924389d3898c' --data "value=12&sensor=moisture&tree_id=1"


Now you can visit [http://localhost:5000](http://localhost:5000)


