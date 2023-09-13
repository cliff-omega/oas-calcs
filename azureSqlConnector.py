import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# CREATE DATABASE CONNECTION URI  
connectionUri = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=sqlhost.database.windows.net;DATABASE=pythonSQL;UID=username@sqldb;PWD=password56789")


# INITIALIZE FLASK APP AND CONFIGURE CONNECTION TO SQL SERVER
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % connectionUri
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# STORE APP AND ITS CONFIGURED SQL CONNECTION AS A VARIABLE
sqlDb = SQLAlchemy(app)

def connectAndWriteToAzureSql(contentsToWrite):
    print('connectAndWriteToAzureSql function was passed the following parameters:')
    print(contentsToWrite)
    return