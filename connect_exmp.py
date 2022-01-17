from unicodedata import name
import cx_Oracle
import sys

#create connection

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:/Users/User/Documents/instantclient-basic-windows.x64-21.3.0.0.0/instantclient_21_3")
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)

# conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
# print(conn.version)

# create cursor


# cur = conn.cursor()
# cur.execute("delete from employee where emp_id = {}".format(id))

def empLst():
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from employee")
    empLst = cur.fetchall()
    # print(empLst)
    return empLst

def secLst():
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from sections")
    secLst = cur.fetchall()
    # print(secLst)
    return secLst

def cusLst():
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from customer")
    cusLst = cur.fetchall()
    # print(cusLst)
    return cusLst

def supLst():
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from supplier")
    supLst = cur.fetchall()
    # print(supLst)
    return supLst

def cloLst():
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("select * from cloth")
    cloLst = cur.fetchall()
    # print(cloLst)
    return cloLst



# print(empLst,secLst,cusLst,supLst,cloLst)

# dname = ""
# cur.execute("insert into department (DNO, DNAME,mgrssn) values (:dept_id, :dept_name,:mgr)", dept_id=220,dept_name=dname,mgr=102)

# cur.execute("select * from employee where emp_id = 101")
# lst = cur.fetchone()
# print(lst[0])

# addre = 'Bang'
# sex = 'm'
# emp_id = '1'

# sql = "update employee set address = :1 , sex = :2 where emp_id = :3"
# cur.execute(sql,[addre, sex , emp_id])

# conn.commit()
# conn.close()