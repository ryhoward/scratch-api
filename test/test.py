import sys
import requests
from csv import reader

users={}

def get_user(id)
    url = 'http://164.90.253.239:5000/users/' + id
    r = requests.get(url)
    if r.status_code == 200:
        return r.content

def publish_data(name):
    url = 'http://164.90.253.239:5000/users'
    payload = '{"user":"ryan_howard"}'#open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    print(r)

def get_data(data):
    if data is not None:
    with open(data, 'r') as read_obj:
        test_data_reader = reader(read_obj)
        iteration=0
        for row in test_data_reader:
            #print(row[1])
            print(row)
            if (iteration == 0):
                continue
            publish_data(row[1])
            users.update({row[0], row[1]})

def find_users():
    for key in users:
        name = get_user(key)
        if name != users[key]
        print('user not found for: ' + key)
        sys.exit(os.EX_SOFTWARE)



test_data = sys.argv[1]
get_data(test_data)
results = find_users()


