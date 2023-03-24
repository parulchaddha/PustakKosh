from flask import Flask,render_template,request,redirect,url_for,session,jsonify
import db_service
from flask_mysqldb import MySQL
#from flask_bcrypt import Bcrypt

app = Flask(__name__)




@app.route('/get_all_books',methods={'GET'})
def get_all_books():
    """ 
    to fetch 
    """
    
    user_id = request.args.get('user_id')
    donation_status = request.args.get('donation_status')
   
    result = db_service.get_all_books(user_id, donation_status)
   
    return jsonify(result)




@app.route('/add_new_book',methods={'POST'})
def add_new_book():
#    if request.method=='POST':
   
    data=request.get_json()
    user_id = data['user_id']
    book_name=data['book_name']
    author=data['author']
    genre=data['genre']
    description=data['description']

    donation_status = data['donation_status']
    result=db_service.add_new_book(user_id, book_name, author, genre, description, donation_status)
    return jsonify(result)

@app.route('/update_request_for_book',methods={'POST'})
def update_request_for_book():
#    if request.method=='POST':
   
    data=request.get_json()
    request_user_id = data['user_id']
    book_id=data['book_id']
    

    
    result=db_service.update_request_for_book(book_id,request_user_id)
    return jsonify(result)


@app.route('/get_requested_items',methods={'GET'})
def get_requested_items():

    # get query params
    # how to get get parameter and post parameter from flast request object
    request_user_id = request.args.get('user_id')
    
    # print(user_id,donation_status)
    result = db_service.get_requested_items(request_user_id)
    # result={"user_id":user_id}
    return jsonify(result)

@app.route('/get_needy_info',methods={'GET'})
def get_needy_info():

    # get query params
    # how to get get parameter and post parameter from flast request object
    book_id = request.args.get('book_id')
    
    # print(user_id,donation_status)
    result = db_service.get_needy_info(book_id)
    print(result)
    # result={"user_id":user_id}
    return jsonify(result)
@app.route('/accept_book_request',methods={'POST'})
def accept_book_request():
#    if request.method=='POST':
   
    data=request.get_json()
    request_id = data['request_id']
    book_id=data['book_id']
    

    
    result=db_service.accept_book_request(book_id,request_id)
    return jsonify(result)


       
if __name__=='__main__':
    app.run(debug=True)
