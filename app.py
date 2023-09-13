import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

# IMPORT HELPER FUNCTIONS HERE
from calculations import outputJson

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

# @app.route('/retool-app')
# def retoolDisplay():
#    return render_template('retool-app.html')

@app.route('/helloworld')
def helloWorld():
   print('app.route for Hello page triggered!')
   return render_template('hello.html')

@app.route('/',methods = ['GET','POST'])
def send():
   if request.method == 'POST':
      formContent = request.form
      ein = request.form['ein']
      print('app.route POST triggered on submit!')
      outputJson(formContent)
      return render_template('hello.html',someText=ein)
   return render_template('index.html')


if __name__ == '__main__':
   app.run()
