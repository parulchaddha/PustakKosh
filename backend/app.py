from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='10082003'
app.config['MYSQL_DB']='pustakkosh'
mysql=MySQL(app)
@app.route('/',methods={'GET','POST'})
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
        return 'welcome'
    return render_template('index.html')

        
if __name__=='main':
    app.run(debug=True)