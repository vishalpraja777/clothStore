from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import connect_exmp
import addData



# Add Employee
def addEmp():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(empIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            empId = empIdEtr.get()
        if(empNameEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee Name cannot be Empty')
        else:
            empName = empNameEtr.get()
        if(addressEtr.get() == ''):
            address = ''
        else:
            address = addressEtr.get()
        if(empSexEtr.get() == ''):
            sex = ''
        else:
            sex = empSexEtr.get()
        if(empSalEtr.get() == ''):
            salary = ''
        else:
            salary = empSalEtr.get()
        if(phoneEtr.get() == ''):
            phoneNo = ''
        else:
            phoneNo = phoneEtr.get()

        if(empMgridEtr.get() == ''):
            mgrId = ''
        else:
            mgrId = empMgridEtr.get()
        if(empSecEtr.get() == ''):
            secNo = ''
        else:
            secNo = empSecEtr.get()
        
        # print(empId + " " + empName + " " +address + " " +sex + " " + salary + " " +phoneNo + " " +mgrId + " " + secNo)
        # print(type(salary))

        addData.addEmployee(empId,empName,address,sex, salary,phoneNo,mgrId, secNo)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10).grid(column=0, row=0)
    empIdEtr = Entry(frm)
    empIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Employee Name:",padding=10).grid(column=0, row=1)
    empNameEtr = Entry(frm)
    empNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=2)
    addressEtr = Entry(frm)
    addressEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Sex:",padding=10).grid(column=0, row=3)
    sex = ['M' , 'F']
    empSexEtr = ttk.Combobox(frm,values=sex,width=15)
    empSexEtr.grid(column = 1, row = 3 )

    ttk.Label(frm, text="Salary:",padding=10).grid(column=0, row=4)
    empSalEtr = Entry(frm)
    empSalEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="Phone No:",padding=10).grid(column=0, row=5)
    phoneEtr = Entry(frm)
    phoneEtr.grid(column = 1, row = 5)

    ttk.Label(frm, text="Manager ID:",padding=10).grid(column=0, row=6)
    empMgridEtr = Entry(frm)
    empMgridEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="Section No:",padding=10).grid(column=0, row=7)
    empSecEtr = Entry(frm)
    empSecEtr.grid(column = 1, row = 7)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=8)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=8)

    window.mainloop()

# Add Section
def addSec():

    def cancelBtn():
        window.destroy()

    def addBtn():

        if(secNoEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Section No cannot be Empty')
        else:
            secNo = secNoEtr.get()
        
        if(secNameEtr.get() == ''):
            secName = ''
        else:
            secName = secNameEtr.get()
        
        if(secLocEtr.get() == ''):
            secLoc = ''
        else:
            secLoc = secLocEtr.get()
        
        if(mgrIdEtr.get() == ''):
            mgrId = ''
        else:
            mgrId = mgrIdEtr.get()

        addData.addSection(secNo,secName,secLoc,mgrId)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Section")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Section No:",padding=10).grid(column=0, row=0)
    secNoEtr = Entry(frm)
    secNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Section Name:",padding=10).grid(column=0, row=1)
    secNameEtr = Entry(frm)
    secNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Section Location:",padding=10).grid(column=0, row=2)
    secLocEtr = Entry(frm)
    secLocEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Manager ID:",padding=10).grid(column=0, row=3)
    mgrIdEtr = Entry(frm)
    mgrIdEtr.grid(column = 1, row = 3)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=4)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=4)

    window.mainloop()

# Add Customer
def addCus():

    def cancelBtn():
        window.destroy()

    def addBtn():

        if(cusIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Customer ID cannot be Empty')
        else:
            cusId = cusIdEtr.get()
        if(cusNameEtr.get() == ''):
            cusName = ''
        else:
            cusName = cusNameEtr.get()
        if(phoNoEtr.get() == ''):
            phoneNo = ''
        else:
            phoneNo = phoNoEtr.get()
        if(mailEtr.get() == ''):
            mail = ''
        else:
            mail = mailEtr.get()
        if(cusSexEtr.get() == ''):
            sex = ''
        else:
            sex = cusSexEtr.get()

        addData.addCustomer(cusId, cusName, phoneNo, mail, sex)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=0)
    cusIdEtr = Entry(frm)
    cusIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Customer Name:",padding=10).grid(column=0, row=1)
    cusNameEtr = Entry(frm)
    cusNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Phone no:",padding=10).grid(column=0, row=2)
    phoNoEtr = Entry(frm)
    phoNoEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Mail:",padding=10).grid(column=0, row=3)
    mailEtr = Entry(frm)
    mailEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Sex:",padding=10).grid(column=0, row=4)
    sex = ['M' , 'F']
    cusSexEtr = ttk.Combobox(frm,values=sex,width=15)
    cusSexEtr.grid(column = 1, row = 4 )

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)

    window.mainloop()

# Add Supplier
def addSup():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(supIdEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Supplier ID cannot be Empty')
        else:
            supId = supIdEtr.get()
        if(phoNoEtr.get() == ''):
            phoneNo = ''
        else:
            phoneNo = phoNoEtr.get()
        if(comEtr.get() == ''):
            company = ''
        else:
            company = comEtr.get()
        if(addressEtr.get() == ''):
            address = ''
        else:
            address = addressEtr.get()
        if(mailEtr.get() == ''):
            mail = ''
        else:
            mail = mailEtr.get()

        addData.addSupplier(supId, phoneNo, company, address, mail)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Supplier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Supplier ID:",padding=10).grid(column=0, row=0)
    supIdEtr = Entry(frm)
    supIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Phone no:",padding=10).grid(column=0, row=1)
    phoNoEtr = Entry(frm)
    phoNoEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Company:",padding=10).grid(column=0, row=2)
    comEtr = Entry(frm)
    comEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=3)
    addressEtr = Entry(frm)
    addressEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Mail:",padding=10).grid(column=0, row=4)
    mailEtr = Entry(frm)
    mailEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)


    window.mainloop()

# Add Cloth
def addClo():

    def cancelBtn():
        window.destroy()

    def addBtn():
        if(cloNoEtr.get() == ''):
            messagebox.showwarning(title='Primary Key', message='Employee ID cannot be Empty')
        else:
            cloNo = cloNoEtr.get()
        if(cloTypeEtr.get() == ''):
            cloType = ''
        else:
            cloType = cloTypeEtr.get()
        if(cloSizeEtr.get() == ''):
            cloSize = ''
        else:
            cloSize = cloSizeEtr.get()
        if(cateEtr.get() == ''):
            category = ''
        else:
            category = cateEtr.get()
        if(comEtr.get() == ''):
            company = ''
        else:
            company = comEtr.get()
        if(priEtr.get() == ''):
            price = ''
        else:
            price = priEtr.get()

        if(cusIdEtr.get() == ''):
            cusId = ''
        else:
            cusId = cusIdEtr.get()
        if(supIdEtr.get() == ''):
            supId = ''
        else:
            supId = supIdEtr.get()
        if(secNoEtr.get() == ''):
            secNo = ''
        else:
            secNo = secNoEtr.get()

        addData.addCloth(cloNo, cloType, cloSize, category, company, price, cusId, supId, secNo)

        messagebox.showinfo(title="Row Added",message="1 Row Added")
        window.destroy()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Add New Cloth")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="Cloth No:",padding=10).grid(column=0, row=0)
    cloNoEtr = Entry(frm)
    cloNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Cloth Type:",padding=10).grid(column=0, row=1)
    cloTypeEtr = Entry(frm)
    cloTypeEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Cloth Size:",padding=10).grid(column=0, row=2)
    cloSizeEtr = Entry(frm)
    cloSizeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Category:",padding=10).grid(column=0, row=3)
    cateEtr = Entry(frm)
    cateEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Company:",padding=10).grid(column=0, row=4)
    comEtr = Entry(frm)
    comEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="Price:",padding=10).grid(column=0, row=5)
    priEtr = Entry(frm)
    priEtr.grid(column = 1, row = 5)

    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=6)
    cusIdEtr = Entry(frm)
    cusIdEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="Supplier ID:",padding=10).grid(column=0, row=7)
    supIdEtr = Entry(frm)
    supIdEtr.grid(column = 1, row = 7)

    ttk.Label(frm, text="Section no:",padding=10).grid(column=0, row=8)
    secNoEtr = Entry(frm)
    secNoEtr.grid(column = 1, row = 8)

    ttk.Button(frm, text="Add", command=addBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)

    window.mainloop()