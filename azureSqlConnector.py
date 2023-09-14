import os
import urllib.parse 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (select, create_engine)

# # CREATE DATABASE CONNECTION URI  
# connectionUri = urllib.parse.quote_plus("Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql-oas.database.windows.net,1433;")


# # INITIALIZE FLASK APP AND CONFIGURE CONNECTION TO SQL SERVER
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'supersecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % connectionUri
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# # STORE APP AND ITS CONFIGURED SQL CONNECTION AS A VARIABLE
# sqlDb = SQLAlchemy(app)

# session = Session(engine)
# selectQuery = select(dbo.Comments).limit(5).all()


# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


def connectAndWriteToAzureSql(contentsToWrite):
    print('connectAndWriteToAzureSql function was passed the following parameters:')
    print(contentsToWrite)
    return

