# flask_web/app.py

#From flask import Flask
import os
from flask import jsonify, request, Flask

app = Flask(__name__)

@app.route('/users',methods = ['POST', 'GET'])
def users():
   if request.method == 'POST':
      user = request.form['nm']
      return 'create user'
   else:
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

