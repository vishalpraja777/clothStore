import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import viewAll

def selectData(tabName,idName,id):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from {} where {} = {}'.format(tabName,idName,id))
    lst = cur.fetchone()
    conn.commit()
    conn.close()
    return lst

def updateEmp(empId,empName,address,sex, salary,phoneNo,mgrId, secNo):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update employee set EMP_NAME = :name, ADDRESS = :addre, SEX = :s, SALARY = :sal, PHONE_NO = :phone, MGR_ID = :mgr, SEC_NO = :sec
        where EMP_ID = :id""",
        name=empName, addre=address, s=sex, sal=salary, phone=phoneNo, mgr=mgrId, sec=secNo, id=empId)
    conn.commit()
    conn.close()

def updateSec(secNo,secName,secLoc,mgrId):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update sections set SEC_NAME = :name, SEC_LOCATION = :loc, MGR_ID = :id
    where SEC_NO = :no""",
    no=secNo, name=secName, loc=secLoc, id=mgrId)
    conn.commit()
    conn.close()

def updateCus(cusId, cusName, phoneNo, mail, sex):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update customer set CUST_NAME = :name, PHONE_NO = :pho, MAIL = :mai, SEX = :s
    where CUST_ID = :id""",
    id=cusId, name=cusName, pho=phoneNo, mai=mail, s=sex)
    conn.commit()
    conn.close()

def updateSup(supId, phoneNo, company, address, mail):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
    update supplier set PHONE_NO = :pho, COMPANY = :comp, ADDERESS = :addre, MAIL = :mai
    where SUPP_ID = :id""",
    id=supId, pho=phoneNo, comp=company, addre=address, mai=mail)
    conn.commit()
    conn.close()

def updateClo(cloNo, cloType, cloSize, category, company, price, cusId, supId, secNo):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute("""
        update cloth set CLOTH_TYPE = :type, CLOTH_SIZE = :siz, CATEGORY = :cate, COMPANY = :comp, PRICE = :price, CUST_ID = :cus, SUPP_ID = :sup, SEC_NO = :sec
        where CLOTH_NO = :no""",
        no=cloNo, type=cloType, siz=cloSize, cate=category, comp=company, price=price, cus=cusId, sup=supId, sec=secNo)
    conn.commit()
    conn.close()
