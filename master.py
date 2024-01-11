import pypyodbc as odbc

def sql_connect():
    driver_name = 'SQL Server' #input("Enter driver name: ") # 
    server_name = 'DESKTOP-KCNLG79' #input("Enter server name: ") #'
    database_name = 'MCE' #input("Enter database name: ")
    trust = 'yes' #input("Trust_connection(yes/no): ")
    try:
        conn = odbc.connect(
            driver= driver_name,
            server= server_name,
            database= database_name,
            Trust_connection= trust
            )
        return conn
    except:
        print("Invalid credential!!!")

def sql_connection_close():
    sql_connect().close()
    print("Connection successfully closed...")

def insert_record():
    sql_qry = "insert into STUDENTS values (?, ?, ?, ?)"
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    fees = int(input("Enter Fees: "))
    params = [id, name, branch, fees]    
    try:
        curobj.execute(sql_qry, params)
        sql_connect().commit()
        print(curobj.rowcount, "rows inserted...")
    except:
        sql_connect().rollback()
        print("Unable to insert record!!!")
    sql_connection_close()

def fetch_record():
    sql_qry = input("Enter select Query(column names: S_ID, S_NAME, BRANCH, FEES) and (Table name: studentS): ")
    try:
        curobj.execute(sql_qry)
        row = curobj.fetchall()
        for i in row:
            print(i)
    except:
        print("Unable to fetch data!!!")
    sql_connection_close()

def update_record():
    sql_qry = input("Enter Update Query(column names: S_ID, S_NAME, BRANCH, FEES) and (Table name: students): ")
    try:
        curobj.execute(sql_qry)
        sql_connect().commit()
        print(curobj.rowcount, "row updated...")
    except:
        sql_connect().rollback()
        print("Unable to Update!!!")
    sql_connection_close()

def delete_record():
    sql_qry = input("Enter Delete Query(column names: S_ID, S_NAME, BRANCH, FEES) and (Table name: student): ")
    try:
        curobj.execute(sql_qry)
        sql_connect().commit()
        print(curobj.rowcount, "row deleted...")
    except:
        sql_connect().rollback()
        print("Unable to delete!!!")
    sql_connection_close()


while True:
    if sql_connect().connected:
        print("connection established...")
    curobj = sql_connect().cursor()
    action = input("Whats action perform(select, delete, update, insert)?: ")
    if 'select' == action:
        fetch_record()
    elif 'delete' == action:
        delete_record()
    elif 'update' == action:
        update_record()
    elif 'insert' == action:
        insert_record()
    else:
        print("Command not Found!!!")
        sql_connection_close()
    exit = input("Do you want to exit(yes/no)?: ")
    if exit == 'yes':
        break