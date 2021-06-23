import os
import sys
import json
import logging
from flask import jsonify, request, Flask, Response
import mysql.connector

class DBManager:
    def __init__(self, database='users', host="users-db", user="root", password_path=None):
        self.connection = mysql.connector.connect(
            user=user, 
            password=os.environ['MYSQL_ROOT_PASSWORD'],
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()
   
    ### Initial db setup and adding of users table
    def db_setup(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
        self.connection.commit()

    ### Get all Users in users table
    def get_users(self):
        self.cursor.execute('SELECT id, name FROM users')
        return self.cursor.fetchall()

    ### get single user by provided id
    def get_user(self, id):
        self.cursor.execute('SELECT name FROM users WHERE id = {0}'.format(id))
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    ### add single user with provided username string
    def add_user(self, name):
        val=(name,)
        query="""INSERT INTO users (name) VALUES (%s)"""
        self.cursor.execute(query, val)
        self.connection.commit()


app = Flask(__name__)
conn = None

### Get either all users or post to create new user
@app.route('/users',methods = ['POST', 'GET'])
def users(name='default'):
        global conn
        if not conn:
            conn = db_connection()
        if request.method == 'POST':            
            if ((request.is_json) and (request.headers['Content-Type'] == 'application/json')):
                username = request.json.get('user', None)
                json_username = json.dumps(username)
                conn.add_user(json_username)
                return 'user created'
            return 'request not in correct json format'
        else:
            rec = conn.get_users()
            response = ''
            users=[]
            for row in rec:
            ### this is never how you want to do this, it shouldn't be a string, but rather a dictionary preferably. I had some issues with pythons/flasks strange transtion and conversion of dictionaries/lists to json.
                response = response  + '{0}, '.format(row)
            return response

### Get any user by id
@app.route('/users/<user_id>')
def users_id(user_id):
    global conn
    if not conn:
        conn = db_connection()
    rec = conn.get_user(user_id)
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
