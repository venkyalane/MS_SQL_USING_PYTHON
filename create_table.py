import pypyodbc as odbc

try:
    # create connection
    conn = odbc.connect(
        driver= 'SQL Server',
        server= 'DESKTOP-KCNLG79',
        database= 'MCE',
        Trust_connection= 'yes'
        )
    print("connection established...")
except:
    print("Unable to connect!!!!")

#create cursor object
curobj = conn.cursor()

#write qry
qry = """create table customer(c_id int,
                               c_name varchar(20))"""
try:
    curobj.execute(qry)
    conn.commit()
    print("table created...")
except:
    conn.rollback()
    print("unable to create")