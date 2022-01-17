import cx_Oracle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import viewAll
import updateData

def delData(tabName,idName,id):
    conn = cx_Oracle.connect('vishal/vishal7@//localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('delete from {} where {} = {}'.format(tabName,idName,id))
    conn.commit()
    conn.close()

def delEmpUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('employee', 'emp_id' , id) != None):
                delData('employee', 'emp_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewEmp()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewEmp()

    window = Tk()
    window.title("Delete Employee")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Employee ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delSecUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('sections', 'sec_no' , id) != None):
                delData('sections', 'sec_no' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewSec()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewSec()

    window = Tk()
    window.title("Delete Section")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Section No to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delCusUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('customer', 'cust_id' , id) != None):
                delData('customer', 'cust_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewCus()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCus()

    window = Tk()
    window.title("Delete Customer")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Customer ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delSupUI():
    
    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('supplier', 'supp_id' , id) != None):
                delData('supplier', 'supp_id' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewSup()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewSup()

    window = Tk()
    window.title("Delete Supplier")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Supplier ID to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def delCloUI():

    def btnDelCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('cloth', 'cloth_no' , id) != None):
                delData('cloth', 'cloth_no' , id)
                messagebox.showinfo(title='Deleted', message='Row with ID:{} deleted'.format(id))
                window.destroy()
                viewAll.viewClo()
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
        
    
    def btnCanClick():
        window.destroy()
        viewAll.viewClo()

    window = Tk()
    window.title("Delete Cloth")

    frm = ttk.Frame(window,padding=20)
    frm.grid()

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Cloth No to delete:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Delete", command=btnDelCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
