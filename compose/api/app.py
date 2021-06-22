import os
import sys
import json
import logging
from flask import jsonify, request, Flask, Response
#from get_docker_secret import get_docker_secret

import mysql.connector


class DBManager:
    ####
    ####
    ####
    def __init__(self, database='users', host="users-db", user="root", password_path=None):
        self.connection = mysql.connector.connect(
            user=user, 
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        #pf.close()
        self.cursor = self.connection.cursor()
    
    def db_setup(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
        self.connection.commit()

    def get_users(self):
        self.cursor.execute('SELECT id, name FROM users')
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute('SELECT name FROM users WHERE id = {0}'.format(id))
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def add_user(self, name):
        val=(name,)
        query="""INSERT INTO users (name) VALUES (%s)"""
        self.cursor.execute(query, val)
        self.connection.commit()


app = Flask(__name__)
conn = None


@app.route('/users',methods = ['POST', 'GET'])
def users(name='default'):
        global conn
        if not conn:
            conn = db_connection()
        if request.method == 'POST':            
            if ((request.is_json) and (request.headers['Content-Type'] == 'application/json')):
                #username = request.json.get('user', None)
                #return username
                

                #content = request.get_json(force=True)
                #s = "Tuple: {}".format(content[...])
                #return s
                

                #to_json = json.dumps(content)
                #tupper = ''.join(stuff)
                #return tupper

                #name = content[1]

                #myanswer = []
                #for tup1 in range(len(content)):
                #     myanswer.append(tup1)
                #return (myanswer)
                #name = to_json["user"]
                #name = content.get("name")
                #name = content["name"]
                conn.add_user('ryan_user')
                return 'user created'
                #return "JSON Message: " + request.json
            return 'request not in json format'
        else:
            rec = conn.get_users()
            response = ''
            users=[]
            for row in rec:
                #response = response  + 'user:{0}, '.format(c)
                #users.update({c[0], c[1]})
                #users.update({'{}'.format(row[0]), '{}'.format(row[1]) })
                users.append('{}'.format(row))
                #return str(row[0])
                #users.update(c)
            #return response
            #return jsonify(users)
            return Response(json.dumps(users),  mimetype='application/json')

@app.route('/users/<transaction_id>')
def users_id(transaction_id):
    global conn
    if not conn:
        conn = db_connection()
    rec = conn.get_user(transaction_id)
    response = ''
    for i in rec:
        response = response + 'user:{0}, '.format(i)
    return response

def db_connection():
    global conn
    if not conn:
        conn = DBManager()
        conn.db_setup()
        return conn

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
