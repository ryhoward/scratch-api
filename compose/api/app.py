import os
from flask import jsonify, request, Flask
#from get_docker_secret import get_docker_secret

import mysql.connector



class DBManager:
    def __init__(self, database='users', host="db", user="root", password_path=None):
        #pw_path = open(password_file, 'r')
        #db_secret = get_docker_secret('root_db_pw', default='test-secret')
        db_secret = os.getenv('MYSQL_ROOT_PASSWORD') 
        self.connection = mysql.connector.connect(
            user=user, 
            #password=pw_path.read(),
            #password=db_secret,
            password="db-78n9n",
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

    def get_users(self):
        self.cursor.execute('SELECT name FROM users')
        items = []
        for d in self.cursor:
            items.append(d[0])
        return items

    def get_user(self, id):
        self.cursor.execute('SELECT name FROM users WHERE id = %s', id)
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def add_user(self, name):
        self.cursor.execute('INSERT INTO users (name) VALUES (%s);', name)
        self.connection.commit()


app = Flask(__name__)
conn = None


@app.route('/users/<name>',methods = ['POST', 'GET'])
def users(name='default'):
        global conn
        if not conn:
            conn = db_connection()#DBManager()
        
        if request.method == 'POST':
            conn.add_user(name)
            return 'user created'
        else:
            rec = conn.get_users()
            response = ''
            for c in rec:
                response = response  + '<div>   Hello  ' + c + '</div>'
            return response
            return users
            #return 'GET users'

@app.route('/users/<transaction_id>')
def users_id(transaction_id):
    return 'get user by id {}'.format(transaction_id)


def db_connection():
    global conn
    if not conn:
        conn = DBManager()#password_path='/run/secrets/root-db-pw')
        conn.db_setup()
        return conn

#@app.route('/')
#def hello_world():
#    return 'Hey, we have Flask in a Docker container!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
