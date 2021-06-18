import os
from flask import jsonify, request, Flask
from get_docker_secret import get_docker_secret

import mysql.connector



class DBManager:
    def __init__(self, database='users', host="db", user="root"):
        #pf = open(password_file, 'r')
        db_secret = get_docker_secret('root-db-pw', default='test-secret')
        self.connection = mysql.connector.connect(
            user=user, 
            password=db_secret,
            host=host, # name of the mysql service as set in the docker-compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        #pf.close()
        self.cursor = self.connection.cursor()
    
    def db_setup(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.cursor.execute('CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
        #self.cursor.executemany('INSERT INTO users (id, name) VALUES (%s, %s);', [(i, 'user name #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def get_user(self):
        self.cursor.execute('SELECT name FROM users WHERE id')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def add_user(self, name):
        self.cursor.execute('INSERT INTO users (name) VALUES (%s);', name)
        self.connection.commit()


app = Flask(__name__)

@app.route('/users',methods = ['POST'])
def users(name):
    if request.method == 'POST':
        user = request.form['nm']
        global conn
        if not conn:
            conn = DBManager()
            conn.add_user(name)
        return 'create user'


@app.route('/users',methods = ['GET'])
def users(id):
    global conn
    if not conn:
        conn = DBManager()
        conn.get_user()
    user = request.args.get('nm')
     return 'get user'


@app.route('/users/<transaction_id>')
def users_id():
    return 'get user by id {}'.format(transaction_id)


#@app.route('/')
#def hello_world():
#    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

