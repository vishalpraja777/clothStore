import cx_Oracle

def addEmployee(empId,empName,address,sex, salary,phoneNo,mgrId, secNo):
    # print(empId + " " + empName + " " +address + " " +sex + " " + salary + " " +phoneNo + " " +mgrId + " " + secNo)
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        insert into employee (EMP_ID, EMP_NAME, ADDRESS, SEX, SALARY, PHONE_NO, MGR_ID, SEC_NO) 
        values (:id, :name, :addre, :s, :sal, :phone, :mgr, :sec)""",
        id=empId, name=empName, addre=address, s=sex, sal=salary, phone=phoneNo, mgr=mgrId, sec=secNo)
    conn.commit()
    conn.close()

def addSection(secNo,secName,secLoc,mgrId):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into sections (SEC_NO, SEC_NAME, SEC_LOCATION, MGR_ID)
    values (:no, :name, :loc, :id)""",
    no=secNo, name=secName, loc=secLoc, id=mgrId)
    conn.commit()
    conn.close()

def addCustomer(cusId, cusName, phoneNo, mail, sex):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into customer (CUST_ID, CUST_NAME, PHONE_NO, MAIL, SEX)
    values (:id, :name, :pho, :mai, :s)""",
    id=cusId, name=cusName, pho=phoneNo, mai=mail, s=sex)
    conn.commit()
    conn.close()

def addSupplier(supId, phoneNo, company, address, mail):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    insert into supplier (SUPP_ID, PHONE_NO, COMPANY, ADDERESS, MAIL)
    values (:id, :pho, :comp, :addre, :mai)""",
    id=supId, pho=phoneNo, comp=company, addre=address, mai=mail)
    conn.commit()
    conn.close()

def addCloth(cloNo, cloType, cloSize, category, company, price, cusId, supId, secNo):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        insert into cloth (CLOTH_NO, CLOTH_TYPE, CLOTH_SIZE, CATEGORY, COMPANY, PRICE, CUST_ID, SUPP_ID, SEC_NO) 
        values (:no, :type, :siz, :cate, :comp, :price, :cus, :sup, :sec)""",
        no=cloNo, type=cloType, siz=cloSize, cate=category, comp=company, price=price, cus=cusId, sup=supId, sec=secNo)
    conn.commit()
    conn.close()