
#a simple Flask app code written by Vas Kuruganti


from flask import Flask, jsonify
from flask_accept import accept, accept_fallback
from flask import request
#from flask import *
app = Flask(__name__)



#@app.route('/')
@accept_fallback
#def hello_world():
#    return '<p>Hello, World</p>'

@app.route('/login',methods = ['GET', 'POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname=="vkuruganti" and passwrd=="auto":
        return "Welcome %s" %uname

#@hello_world.support('application/json')
#def hello_world_json():
#    return jsonify(message="Hello, World")


if __name__ == '__main__':
    app.run()
