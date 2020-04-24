import requests
import random
import datetime



headers = {'Authorization': 'Token 658e9405f5681018e101c3ceba43924389d3898c'}

print('adding random sensor measurement')

data = {'value': random.randint(0,40),'sensor':'test','tree_id':0, 'when' : datetime.date.today() - datetime.timedelta(minutes=random.randint(0,120))}
r = requests.post('http://127.0.0.1:5000/add_measurement/',data=data, headers=headers)
print(r.headers)
print(r.json())


print('print all sensor measurements')
r = requests.get('http://127.0.0.1:5000/measurements/')
print(r.headers)
print(r.json())