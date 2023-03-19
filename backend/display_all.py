from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

display_all = Flask(__name__)
display_all.config['MYSQL_HOST'] = 'localhost'
display_all.config['MYSQL_USER'] = 'root'
display_all.config['MYSQL_PASSWORD'] = '10082003'
display_all.config['MYSQL_DB'] ='pustakkosh'
mysql = MySQL(display_all)
bcrypt = Bcrypt(display_all)

display_all.secret_key="super secret key"
@display_all.route('/',methods={'GET','POST'})
def display_books():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM book"
    cur.execute(query)
    books = cur.fetchall()
    print("All Available Books: ")
    for book in books:
        print(book)
    cur.close()
    
if __name__=='main':
    display_all.run(debug=True)
