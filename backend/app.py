from flask import Flask,render_template,request,redirect,url_for,session,jsonify
import db
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='10082003'
app.config['MYSQL_DB']='pustakkosh'
mysql=MySQL(app)
bcrypt=Bcrypt(app)



@app.route('/get_all_books',methods={'GET'})
def get_all_books():
    print(request.args)





# cur=mysql.connection.cursor()
app.secret_key="super secret key"
@app.route('/register',methods={'GET','POST'})
def index():

    
    if request.method=='POST':
        userdetails=request.form
        name=userdetails['name']
        password=userdetails['password']
        location=userdetails['location']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO user(user_name,user_pass,location) VALUES(%s,%s,%s)",(name,password,location))
        
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('index.html')
@app.route('/login',methods={'GET','POST'})

def login():

    
    if request.method=='POST':
        
        userdetails=request.form
        name=userdetails['name']
        password=userdetails['password']
        print(name,password)
        cur=mysql.connection.cursor()
        cur.execute('SELECT *FROM user WHERE user_name=%s AND user_pass=%s',(name,password))
        record=cur.fetchone()
        print(record)
        if record:
            print('1')
            session['loggedin']=True
            session['user_id']=record[0]
            return redirect(url_for('book'))
        else:
            msg="INCOREECT DETAILS"
     
       
    return render_template('login.html')

@app.route('/book',methods={'GET','POST'})
def book():
    if request.method=='POST':
        book=request.form
        name=book['name']
        author=book['author']
        genre=book['genre']
        user_id=session['user_id']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO book(book_name,author,genre,user_id) VALUES(%s,%s,%s,%s)",(name,author,genre,user_id))
        mysql.connection.commit()
        cur.close()
        return 'book_added'
    return render_template('book.html',user_id=session['user_id'])
# @app.route('/test',methods={'GET','POST'})
# def test():
#    d={
#        '1':'book_name','2':'author'
#    }
#    return jsonify(d)

@app.route('/needy_dis',methods={'GET','POST'})
def needy_dis():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM book"
    cur.execute(query)
    books = cur.fetchall()-
    print("All Available Books: ")
    for book in books:
        print(book)
    cur.close()

       
if __name__=='main':
    app.run(debug=True)
