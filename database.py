import sqlite3
username="Chander"
password="jdlkajds"
def create(username,password):
        
    conn=sqlite3.connect("automation.db")

    try:
        conn.execute('''CREATE TABLE facebook
             (Username Text PRIMARY KEY     NOT NULL,
             Password           TEXT    NOT NULL);''')
        
        conn.execute("INSERT INTO facebook ('Username','Password') \
          VALUES (?,?)",(username,password));
        print("Facebook data created and saved successfully")
    except:
        conn.execute("INSERT INTO facebook ('Username','Password') \
          VALUES (?,?)",(username,password))
        
        b=conn.execute("select * from facebook")
        for i in b:
            print("username",i[0])
            print("password",i[1])
        print("new user data inserted")
    conn.close()
create(username,password)

def facebook():
    username=""
    password=""
    conn=sqlite3.connect("automation.db")
    b=conn.execute("select * from facebook")
    for i in b:
        username=i[0]
        password=i[1]
        print("username",i[0])
        print("password",i[1])
        print("new user data inserted")
    
    return username,password
    conn.close()
facebook()
