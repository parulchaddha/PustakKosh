from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

search_book = Flask(__name__)
search_book.config['MYSQL_HOST'] = 'localhost'
search_book.config['MYSQL_USER'] = 'root'
search_book.config['MYSQL_PASSWORD'] = '10082003'
search_book.config['MYSQL_DB'] ='pustakkosh'
mysql = MySQL(search_book)
bcrypt = Bcrypt(search_book)

search_book.secret_key="super secret key"
@search_book.route('/',methods={'GET','POST'})
def search_book():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        search_string = request.form['search_string']
        cur.execute("SELECT * from book WHERE book_name LIKE %s OR author LIKE %s or genre LIKE %s", (search_string, search_string, search_string))
        mysql.connection.commit()
        results = cur.fetchall()
        if len(results) == 0 and search_string == 'all': 
            cur.execute("SELECT * from book")
            mysql.connection.commit()
            results = cur.fetchall()
        return render_template('search.html', data = results)
    return render_template('search.html')
    
if __name__=='main':
    search_book.run(debug=True)