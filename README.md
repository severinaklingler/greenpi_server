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
```python manage.py collectstatic
   python manage.py migrate
   heroku local web -f Procfile.windows
```
Now you can visit [http://localhost:5000](http://localhost:5000)


