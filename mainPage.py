from tkinter import *
from tkinter import ttk
import addNew
import viewAll


def win():
   # window creation
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("Cloth Store")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Employee
    empRow = 0
    ttk.Label(frm,text="Employee",padding=10).grid(column=0,row=empRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=empRow)

    addEmpBtn = ttk.Button(frm, text="Add New", command=addNew.addEmp)
    addEmpBtn.grid(column=2,row=empRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=empRow)
    
    viewAllEmpBtn = ttk.Button(frm, text="View All", command=viewAll.viewEmp)
    viewAllEmpBtn.grid(column=4,row=empRow)

    # Section
    secRow = 1
    ttk.Label(frm,text="Section",padding=10).grid(column=0,row=secRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=secRow)

    addSecBtn = ttk.Button(frm, text="Add New", command=addNew.addSec)
    addSecBtn.grid(column=2,row=secRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=secRow)
    
    viewAllSecBtn = ttk.Button(frm, text="View All", command=viewAll.viewSec)
    viewAllSecBtn.grid(column=4,row=secRow)

    # Customer
    cusRow = 2
    ttk.Label(frm,text="Customer",padding=10).grid(column=0,row=cusRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=cusRow)

    addCusBtn = ttk.Button(frm, text="Add New", command=addNew.addCus)
    addCusBtn.grid(column=2,row=cusRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=cusRow)
    
    viewAllCusBtn = ttk.Button(frm, text="View All", command=viewAll.viewCus)
    viewAllCusBtn.grid(column=4,row=cusRow)

    # Supplier
    supRow = 3
    ttk.Label(frm,text="Supplier",padding=10).grid(column=0,row=supRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=supRow)

    addSupBtn = ttk.Button(frm, text="Add New", command=addNew.addSup)
    addSupBtn.grid(column=2,row=supRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=supRow)
    
    viewAllSupBtn = ttk.Button(frm, text="View All", command=viewAll.viewSup)
    viewAllSupBtn.grid(column=4,row=supRow)

    # Cloth
    cloRow = 4
    ttk.Label(frm,text="Cloth",padding=10).grid(column=0,row=cloRow)

    ttk.Label(frm,text="",padding=10).grid(column=1,row=cloRow)

    addCloBtn = ttk.Button(frm, text="Add New", command=addNew.addClo)
    addCloBtn.grid(column=2,row=cloRow)

    ttk.Label(frm,text="",padding=10).grid(column=3,row=cloRow)
    
    viewAllCloBtn = ttk.Button(frm, text="View All", command=viewAll.viewClo)
    viewAllCloBtn.grid(column=4,row=cloRow)

    ttk.Button(frm, text="Exit", command=window.destroy).grid(column=2,row=5)

    window.mainloop()