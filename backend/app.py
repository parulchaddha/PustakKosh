from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='10082003'
app.config['MYSQL_DB']='pustakkosh'
mysql=MySQL(app)
bcrypt=Bcrypt(app)

# cur=mysql.connection.cursor()
app.secret_key="super secret key"
@app.route('/register',methods={'GET','POST'})

def index():

    
    if request.method=='POST':
        userdetails=request.form
        name=userdetails['name']
        hashed_password=bcrypt.generate_password_hash(userdetails['password']).decode('utf-8')
        location=userdetails['location']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO user(user_name,user_pass,location) VALUES(%s,%s,%s)",(name,hashed_password,location))
        
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('index.html')
@app.route('/login',methods={'GET','POST'})

def login():

    
    if request.method=='POST':
        userdetails=request.form
        name=userdetails['name']
        hashed_password=bcrypt.generate_password_hash(userdetails['password']).decode('utf-8')
        
        cur=mysql.connection.cursor()
        cur.execute('SELECT *FROM user WHERE user_name=%s AND user_pass=%s',(name,hashed_password))
        record=cur.fetchone()
        if record:
            session['loggedin']=True
            session['user_id']=record[0]
            return redirect(url_for('book'))
        else:
            msg="INCOREECT DETAILS"
     
       
    return render_template('login.html')

@app.route('/book',methods={'GET','POST'})
def books():
    if request.method=='POST':
        book=request.form
        name=book['name']
        author=book['author']
        genre=book['genre']
        user_id=book['user_id']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO book(book_name,author,genre,user_id) VALUES(%s,%s,%s,%s)",(name,author,genre,user_id))
        mysql.connection.commit()
        cur.close()
        return 'book_added'
    return render_template('book.html',user_id=session['user_id'])



       
if __name__=='main':
    app.run(debug=True)
        
