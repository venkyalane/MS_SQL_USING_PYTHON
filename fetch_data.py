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
qry = "select * from STUDENTS"

try:
    curobj.execute(qry)
    row = curobj.fetchall()
    for i in row:
        print(i)
except:
    print("Unable to fetch data!!!")

conn.close()
