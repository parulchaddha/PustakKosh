import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="10082003",
  database="pustakkosh"
)
cur = mydb.cursor()

def get_all_books(user_id=None, donation_status=None):
    # prepare sql query

    # if not None both
    

    
    if user_id==None and donation_status==None:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book "
     rows = cur.execute(query) # list of tuples
    elif user_id==None:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE donation_status=%s"
     rows = cur.execute(query,(donation_status,))
    elif donation_status==None:
     query= "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE user_id=%s"
     print(query)
     cur.execute(query,(user_id,))
     rows=cur.fetchall()
    else:
     query = "SELECT book_id,book_name,author,genre,donation_status,request_count FROM book WHERE user_id=%s and donation_status=%s"
     rows = cur.execute(query,(user_id,donation_status))
    # (1, user_id, name, author, genre, desc, donation_stauts, req_cnt )
    
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
    
    return result

def update_request_for_book(book_id, request_user_id):
    # prepare update query for book table

    select_query = 'SELECT request_count FROM book WHERE book_id=%s'
    cur.execute(select_query,(book_id,))
    cnt=cur.fetchall()

    req_cnt  =cnt[0][0]+ 1
    update_book_q = "UPDATE book SET request_count=%s WHERE book_id=%s"
    cur.execute(update_book_q,(req_cnt,book_id))
    mydb.commit()
    # prepare add to request table

    request_tbl_q = " INSERT INTO request(request_user_id,book_id,queue_order) VALUES(%s,%s,%s)"
    try:
        print('1')
        cur.execute(request_tbl_q,(request_user_id,book_id,req_cnt))
        mydb.commit()
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
update_request_for_book()
def add_new_book(user_id, book_name, author, genre, description, status):
    query = "INSERT INTO book(book_name,description,author,genre,donation_status,user_id) VALUES (%s,%s,%s,%s,%s,%s)"
    try:
        
        cur.execute(query, (book_name, description,
                         author, genre, status, user_id))
        mydb.commit()
    except:
            return {'status': False,'error': "Failed to insert"}
        
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

    
def get_requested_items(request_user_id):
        query="Select * from book left join request on book.book_id=request.book_id WHERE request_user_id=%s"
        cur.execute(query,(request_user_id,))

        myresult = cur.fetchall()
        print(myresult)
        return myresult
