# Author : Vas Kuruganti
from flask import Flask, jsonify
from flask_accept import accept, accept_fallback
from flask import request
import logging
import requests
from flask import Flask, render_template


app = Flask(__name__)  

#app.config["DEBUG"] = True
#logging.basicConfig(filename='demo.log',level=logging.DEBUG)

#app.logger.disabled = True
# reponse for GET request without an accept header
@app.route('/')
@accept_fallback
def hello_world():
    app.logger.info('Processing default request without any accept header')
    return '<p>Hello, World</p>'

#response for GET request with Accept header with value application/json
@hello_world.support('application/json')
def hello_world_json():
    app.logger.info('Processing default request with accept header "application/json"')
    return jsonify(message="Hello, World")



@app.route('/message')
def my_form():
    return(render_template('my-form.html'))

@app.route('/message', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return(processed_text)
  

   
if __name__ == '__main__':  
   app.run() 
