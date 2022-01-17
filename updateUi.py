from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import up
import updateData
import viewAll


# Update Employee
def updateEmpUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewEmp()

    def updateBtn():
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

        updateData.updateEmp(empId,empName,address,sex, salary,phoneNo,mgrId, secNo)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewEmp()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('employee', 'emp_id', id)

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    empIdEtr = Entry(frm)
    empIdEtr.insert(0,str(lst[0]))
    # empIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Employee Name:",padding=10).grid(column=0, row=1)
    empNameEtr = Entry(frm)
    empNameEtr.insert(0,str(lst[1]))
    empNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=2)
    addressEtr = Entry(frm)
    addressEtr.insert(0,str(lst[2]))
    addressEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Sex:",padding=10).grid(column=0, row=3)
    sex = ['M' , 'F']
    empSexEtr = ttk.Combobox(frm,values=sex,width=15)
    empSexEtr.grid(column = 1, row = 3 )

    ttk.Label(frm, text="Salary:",padding=10).grid(column=0, row=4)
    empSalEtr = Entry(frm)
    empSalEtr.insert(0,str(lst[4]))
    empSalEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="Phone No:",padding=10).grid(column=0, row=5)
    phoneEtr = Entry(frm)
    phoneEtr.insert(0,str(lst[5]))
    phoneEtr.grid(column = 1, row = 5)

    ttk.Label(frm, text="Manager ID:",padding=10).grid(column=0, row=6)
    empMgridEtr = Entry(frm)
    empMgridEtr.insert(0,str(lst[6]))
    empMgridEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="Section No:",padding=10).grid(column=0, row=7)
    empSecEtr = Entry(frm)
    empSecEtr.insert(0,str(lst[7]))
    empSecEtr.grid(column = 1, row = 7)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=8)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=8)

    window.mainloop()

# Update Section
def updateSecUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewSec()

    def updateBtn():

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

        updateData.updateSec(secNo,secName,secLoc,mgrId)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewSec()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Section")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('sections', 'sec_no', id)

    # Fields
    ttk.Label(frm, text="Section No:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    secNoEtr = Entry(frm)
    secNoEtr.insert(0,str(lst[0]))
    # secNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Section Name:",padding=10).grid(column=0, row=1)
    secNameEtr = Entry(frm)
    secNameEtr.insert(0,str(lst[1]))
    secNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Section Location:",padding=10).grid(column=0, row=2)
    secLocEtr = Entry(frm)
    secLocEtr.insert(0,str(lst[2]))
    secLocEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Manager ID:",padding=10).grid(column=0, row=3)
    mgrIdEtr = Entry(frm)
    mgrIdEtr.insert(0,str(lst[3]))
    mgrIdEtr.grid(column = 1, row = 3)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=4)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=4)

    window.mainloop()

# Update Customer
def updateCusUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewCus()

    def updateBtn():

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

        updateData.updateCus(cusId, cusName, phoneNo, mail, sex)

        messagebox.showinfo(title="Updated",message="1 Row Updated")
        window.destroy()
        viewAll.viewCus()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('customer', 'cust_id', id)

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    cusIdEtr = Entry(frm)
    cusIdEtr.insert(0,str(lst[0]))
    # cusIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Customer Name:",padding=10).grid(column=0, row=1)
    cusNameEtr = Entry(frm)
    cusNameEtr.insert(0,str(lst[1]))
    cusNameEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Phone no:",padding=10).grid(column=0, row=2)
    phoNoEtr = Entry(frm)
    phoNoEtr.insert(0,str(lst[2]))
    phoNoEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Mail:",padding=10).grid(column=0, row=3)
    mailEtr = Entry(frm)
    mailEtr.insert(0,str(lst[3]))
    mailEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Sex:",padding=10).grid(column=0, row=4)
    sex = ['M' , 'F']
    cusSexEtr = ttk.Combobox(frm,values=sex,width=15)
    cusSexEtr.grid(column = 1, row = 4 )

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)

    window.mainloop()

# Update Supplier
def updateSupUi(id):

    def cancelBtn():
        window.destroy()
        viewAll.viewSup()

    def updateBtn():
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

        updateData.updateSup(supId, phoneNo, company, address, mail)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewSup()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Supplier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('supplier', 'supp_id', id)

    # Fields
    ttk.Label(frm, text="Supplier ID:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    supIdEtr = Entry(frm)
    supIdEtr.insert(0,str(lst[0]))
    # supIdEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Phone no:",padding=10).grid(column=0, row=1)
    phoNoEtr = Entry(frm)
    phoNoEtr.insert(0,str(lst[1]))
    phoNoEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Company:",padding=10).grid(column=0, row=2)
    comEtr = Entry(frm)
    comEtr.insert(0,str(lst[2]))
    comEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Address:",padding=10).grid(column=0, row=3)
    addressEtr = Entry(frm)
    addressEtr.insert(0,str(lst[3]))
    addressEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Mail:",padding=10).grid(column=0, row=4)
    mailEtr = Entry(frm)
    mailEtr.insert(0,str(lst[4]))
    mailEtr.grid(column = 1, row = 4)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=5)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=5)


    window.mainloop()

# Update Cloth
def updateCloUi(id):
    def cancelBtn():
        window.destroy()
        viewAll.viewClo()

    def updateBtn():
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

        updateData.updateClo(cloNo, cloType, cloSize, category, company, price, cusId, supId, secNo)

        messagebox.showinfo(title="Update",message="1 Row Updated")
        window.destroy()
        viewAll.viewClo()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Update Cloth")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    lst = updateData.selectData('cloth', 'cloth_no', id)

    # Fields
    ttk.Label(frm, text="Cloth No:",padding=10).grid(column=0, row=0)
    ttk.Label(frm, text=str(lst[0]),padding=10).grid(column=1, row=0)
    cloNoEtr = Entry(frm)
    cloNoEtr.insert(0,str(lst[0]))
    # cloNoEtr.grid(column = 1, row = 0)

    ttk.Label(frm, text="Cloth Type:",padding=10).grid(column=0, row=1)
    cloTypeEtr = Entry(frm)
    cloTypeEtr.insert(0,str(lst[1]))
    cloTypeEtr.grid(column = 1, row = 1)

    ttk.Label(frm, text="Cloth Size:",padding=10).grid(column=0, row=2)
    cloSizeEtr = Entry(frm)
    cloSizeEtr.insert(0,str(lst[2]))
    cloSizeEtr.grid(column = 1, row = 2)

    ttk.Label(frm, text="Category:",padding=10).grid(column=0, row=3)
    cateEtr = Entry(frm)
    cateEtr.insert(0,str(lst[3]))
    cateEtr.grid(column = 1, row = 3)

    ttk.Label(frm, text="Company:",padding=10).grid(column=0, row=4)
    comEtr = Entry(frm)
    comEtr.insert(0,str(lst[4]))
    comEtr.grid(column = 1, row = 4)

    ttk.Label(frm, text="Price:",padding=10).grid(column=0, row=5)
    priEtr = Entry(frm)
    priEtr.insert(0,str(lst[5]))
    priEtr.grid(column = 1, row = 5)

    ttk.Label(frm, text="Customer ID:",padding=10).grid(column=0, row=6)
    cusIdEtr = Entry(frm)
    cusIdEtr.insert(0,str(lst[6]))
    cusIdEtr.grid(column = 1, row = 6)

    ttk.Label(frm, text="Supplier ID:",padding=10).grid(column=0, row=7)
    supIdEtr = Entry(frm)
    supIdEtr.insert(0,str(lst[7]))
    supIdEtr.grid(column = 1, row = 7)

    ttk.Label(frm, text="Section no:",padding=10).grid(column=0, row=8)
    secNoEtr = Entry(frm)
    secNoEtr.insert(0,str(lst[8]))
    secNoEtr.grid(column = 1, row = 8)

    ttk.Button(frm, text="Update", command=updateBtn).grid(column=0, row=9)
    ttk.Button(frm, text="Cancel", command=cancelBtn).grid(column=1, row=9)

    window.mainloop()


# Dialog Boxes
def updateEmpDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('employee', 'emp_id' , id) != None):
                window.destroy()
                updateEmpUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewEmp()

    window = Tk()
    window.title("Update Employee")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Employee ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateSecDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('sections', 'sec_no' , id) != None):
                window.destroy()
                updateSecUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewSec()

    window = Tk()
    window.title("Update Section")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Section No to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()


def updateCusDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('customer', 'cust_id' , id) != None):
                window.destroy()
                updateCusUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewCus()

    window = Tk()
    window.title("Update Customer")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Customer ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateSupDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('supplier', 'supp_id' , id) != None):
                window.destroy()
                updateSupUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewSup()

    window = Tk()
    window.title("Update Supplier")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Supplier ID to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()

def updateCloDio():

    def btnUpCick():
        id = id_enter.get()
        if(id == ''):
            messagebox.showwarning(title='Empty', message='Enter the ID')
        else:
            if(updateData.selectData('cloth', 'cloth_no' , id) != None):
                window.destroy()
                updateCloUi(id)
            else:
                messagebox.showwarning(title="Not Found",message="ID doesn't exist")
            
    
    def btnCanClick():
        window.destroy()
        viewAll.viewClo()

    window = Tk()
    window.title("Update Cloth")

    frm = ttk.Frame(window,padding=20)
    frm.grid()
    ttk.Label(frm,text="Enter Cloth No to Update:",padding=10).grid(column=0,row=0)
    id_enter = Entry(frm)
    id_enter.grid(column=0,row=1)
    ttk.Label(frm,text="",padding=10).grid(column=0,row=2)
    ttk.Button(frm, text="Update", command=btnUpCick).grid(column=0,row=3)
    ttk.Button(frm, text="Cancel", command=btnCanClick).grid(column=0,row=4)

    window.mainloop()
