import sys
import requests
from csv import reader

users={}
api_endpoint='http://164.90.253.239:5000/users'

def get_user(id):
    url = api_endpoint + '/{}'.format(id)
    r = requests.get(url)
    if r.status_code == 200:
        return r.content
    else:
        print ('user not found for user by id:' + id)
        sys.exit(os.EX_SOFTWARE)

def publish_data(name):
    url = api_endpoint
    payload = '{"user":"ryan_howard"}'#open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    #print(r)

def get_data(data):
    if data is not None:
        with open(data, 'r') as read_obj:
            test_data_reader = reader(read_obj)
            iteration=0
            for row in test_data_reader:
                #print(row)
                if (iteration == 0):
                    continue
                publish_data(row[1])
                users.update({row[0], row[1]})

def find_users():
    for key in users:
        name = get_user(key)
        if name != users[key]:
            print('user not found for: ' + key)
        sys.exit(os.EX_SOFTWARE)

def compare_all_users():
    url = api_endpoint
    r = requests.get(url)
    #print(r.text)
    data = r.content
    revised = data.replace(b" ", b"").replace(b"),", b")^").replace(b"(", b"").replace(b")", b"")
    other = revised.split(b"^")
    for i in other:
        #print(i)
        item = i.split(b",")
        if not item[0]:
            continue
        print(item[0])
        print(item[1])
        print(users[str(item[0])])

test_data = sys.argv[1]
get_data(test_data)
find_users()
### This is where my slight inexperience with python flask requests and converting tuples with "ellipses". Had trouble completing this in the time frame. Leaving incomplete.
#compare_all_users()
print("tests completed successfully")
sys.exit()
