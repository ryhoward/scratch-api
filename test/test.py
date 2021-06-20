import sys
import requests
from csv import reader


def publish_data(name):
    url = 'http://164.90.253.239:5000/users'
    payload = '{"user":"ryan_howard"}'#open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    print(r)



test_data = sys.argv[1]

if test_data is not None:
    with open(test_data, 'r') as read_obj:
        test_data_reader = reader(read_obj)
        for row in test_data_reader:
            print(row[1])
            publish_data(row[1])
    


