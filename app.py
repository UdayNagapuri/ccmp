import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)




@app.route("/")
def search():
    return render_template('index.html')
    
@app.route("/results", methods=['POST','GET'])
def results():
    if request.method=='POST':
        searchString= request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("""SELECT href,id FROM test.input""")
        rv = cur.fetchall()
        print(rv)
        #print(type(rv))
        finalResult=list(rv)
        ff=[]
        for _ in finalResult:
            ff.append(list(_))

        # finalResult=list(list(rv))
        print(finalResult)
        #["kjnfkdn","kjdsf","isnfi","kjksndfsn","kjdfjk","kjdsnfk"]
        return render_template('results.html',results=ff)

    