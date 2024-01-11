import pypyodbc as odbc

try:
    # create connection
    conn = odbc.connect(
        driver= 'SQL Server',
        server= 'DESKTOP-KCNLG79',
        database= 'MCE',
        Trust_connection= 'yes')
    print("connection established...")
except:
    print("Unable to connect!!!!")

conn.close()