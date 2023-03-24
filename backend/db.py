import mysql.connector

def get_db_connection():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="10082003",
  database="pustakkosh"
  )
 
  return mydb

def get_all_books(user_id=None, donation_status=None):
    # prepare sql query

    # if not None both
    
    db_connec=get_db_connection()
    cur = db_connec.cursor()
    if user_id==None and donation_status==None:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book "
    
     cur.execute(query) # list of tuples
     rows=cur.fetchall()
    elif user_id==None:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE donation_status=%s"
     cur.execute(query,(donation_status,))
     rows=cur.fetchall()
    elif donation_status==None:
     query= "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE user_id=%s"
     
     cur.execute(query,(user_id,))
     rows=cur.fetchall()
    else:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE user_id=%s and donation_status=%s"
     cur.execute(query,(user_id,donation_status))
     rows=cur.fetchall()
    
    
    # convert to list of dict
    result = []
    for row in rows:
        
        entry = {
            'book_id': row[0],
            'book_name': row[1],
            'author':row[2],
            'genre':row[3],
            'donation_status':row[4],
            'request_count':row[5]
             

            #...
        }
        
        result.append(entry)
    print(result)
    return result
get_all_books(2)
def update_request_for_book(book_id, request_user_id):
    # prepare update query for book table
    db_connec=get_db_connection()
    cur = db_connec.cursor()
    select_query = 'SELECT request_count FROM book WHERE book_id=%s'
    cur.execute(select_query,(book_id,))
    cnt=cur.fetchall()

    req_cnt  =cnt[0][0]+ 1
    update_book_q = "UPDATE book SET request_count=%s WHERE book_id=%s"
    cur.execute(update_book_q,(req_cnt,book_id))
    db_connec.commit()
    # prepare add to request table

    request_tbl_q = " INSERT INTO request(request_user_id,book_id,queue_order) VALUES(%s,%s,%s)"
    try:
        
        cur.execute(request_tbl_q,(request_user_id,book_id,req_cnt))
        db_connec.commit()
    except:
        return {'status': False, 'error': "Failed to insert"}
    # search the insert request
    search_query="SELECT request_id,request_user_id,book_id,queue_order FROM request WHERE  request_user_id=%s and book_id=%s and queue_order=%s"
    cur.execute(search_query,(request_user_id,book_id,req_cnt))
    rows=cur.fetchall()
    
    print(rows)
    return{
        'stauts': True,
        'request_added': {
            'request_id': rows[0][0],
            'book_id': rows[0][2],
            'queue_order':rows[0][3]
#            ....
        }
    }
# update_request_for_book(7, 1)
# update_request_for_book()
def add_new_book(user_id, book_name, author, genre, description, status):
    db_connec=get_db_connection()
    cur = db_connec.cursor()
    query = "INSERT INTO book(book_name,description,author,genre,donation_status,user_id) VALUES (%s,%s,%s,%s,%s,%s)"
    # try:
        
       
    # except:
    #         return {'status': False,'error': "Failed to insert"}
    cur.execute(query, (book_name, description,
                         author, genre, status, user_id))
    db_connec.commit()   
    query="SELECT book_id,book_name,author,genre,donation_status,user_id,request_count,description from book where book_name=%s and user_id=%s"
    val = (book_name, user_id)
    cur.execute(query, val)
    rows=cur.fetchall()
    print (rows)
    return {
        'status': True,
        'inserted_book': {
            'book_id': rows[0][0],
            'book_name': rows[0][1],
            'author':rows[0][2],
            'genre':rows[0][3],
            'donation_status':rows[0][4],
            'user_id':rows[0][5],
            'request_count':rows[0][6],
            'description':rows[0][7]
        }
    }

# add_new_book(1,'pj','rr','fic','def','pending')
def get_requested_items(request_user_id):
        db_connec=get_db_connection()
        cur = db_connec.cursor()
        query="Select book.book_id,book_name,author,genre,queue_order,request_status,user_name,email_id from book left join request on book.book_id=request.book_id left join user on book.user_id=user.user_id WHERE request_user_id=%s"
        cur.execute(query,(request_user_id,))
        rows=cur.fetchall()
        result = []
        for row in rows:
        
       
          entry = {
            'book_id': row[0],
            'book_name': row[1],
            
            'author':row[2],
            
            'genre':row[3],
            'queue_order':row[4],
            'request_status':row[5],
            'user_name':row[6],
            'email_id':row[7]

             

            #...
            }
        result.append(entry)
        print(result)
        return result
# get_requested_items(1)
def get_needy_info(book_id):
    db_connec=get_db_connection()
    cur = db_connec.cursor()
    query="Select * from request left join user on request.request_user_id=user.user_id WHERE book_id=%s"
    cur.execute(query,(book_id,))
    rows=cur.fetchall()
    result = []
    for row in rows:
        
       
        entry = {
            'request_id': row[0],
            'request_user_id': row[1],
            
            'queue_order':row[3],
            
            'user_name':row[5]
             

            #...
            }
        result.append(entry)
    print(result)
    return result
# get_needy_info(15)
def accept_book_request(book_id,request_id):
    db_connec=get_db_connection()
    cur = db_connec.cursor()
    update_request = "UPDATE request SET request_status=%s WHERE request_id=%s"
    cur.execute(update_request,("COMPLETED",request_id))
    db_connec.commit()
    update_book = "UPDATE book SET donation_status=%s WHERE book_id=%s"
    cur.execute(update_book,("COMPLETED",book_id))
    db_connec.commit()
    result="donation completed"
    return result
      
# accept_book_request(15,49)
