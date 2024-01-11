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
qry = "update students set s_name = ? where s_id = ?"
sname = input("enter new name: ")
sid = int(input("enter id want to change: "))
params = [sname, sid]
try:
    curobj.execute(qry, params)
    conn.commit()
    print(curobj.rowcount, "record updated...")
except:
    conn.rollback()
    print("Unale to update!!!")

conn.close()