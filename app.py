import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/retool-app')
def retoolDisplay():
   return render_template('retool-app.html')

@app.route('/helloworld')
def helloWorld():
   print("Hello, World!")
   return render_template('hello.html')

@app.route('/',methods = ['GET','POST'])
def send():
   if request.method == 'POST':
      formText = request.form['someText']
      return render_template('hello.html',someText=formText)
   return render_template('index.html')


if __name__ == '__main__':
   app.run()
