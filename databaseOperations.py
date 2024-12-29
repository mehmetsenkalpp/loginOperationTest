import sqlite3

def getUserInfo():
    connection_obj = sqlite3.connect('database.db') 
    cursor_obj = connection_obj.cursor() 
    statement = '''SELECT * FROM user'''
    cursor_obj.execute(statement) 
    output = cursor_obj.fetchall() 
    data =[]
    for row in output:
        data.append(row)
    connection_obj.commit() 
    connection_obj.close()
    return data
    