from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10082003'
app.config['MYSQL_DB'] ='pustakkosh'
mysql = MySQL(app)
bcrypt = Bcrypt(app)

app.secret_key="super secret key"
@app.route('/display_all',methods={'GET','POST'})
def display_books():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM book"
    cur.execute(query)
    books = cur.fetchall()
    print("All Available Books: ")
    for book in books:
        print(book)
    cur.close()
