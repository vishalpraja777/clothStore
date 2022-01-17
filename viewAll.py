from tkinter import *
from tkinter import ttk
import connect_exmp
import deleteData
import updateUi

def viewEmp():

    def btnDel():
        window.destroy()
        deleteData.delEmpUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateEmpDio()     

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Employee")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Employee ID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Employee Name:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Address:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Sex:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Salary:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="Phone no:",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    ttk.Label(frm, text="Manager ID:",padding=10,relief="raised").grid(column=12, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
    ttk.Label(frm, text="Section No:",padding=10,relief="raised").grid(column=14, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=15, row=0)


    lst = connect_exmp.empLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
        ttk.Label(frm, text=lst[i][6],padding=10,relief="flat").grid(column=12, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
        ttk.Label(frm, text=lst[i][7],padding=10,relief="flat").grid(column=14, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=15, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=10, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=17, row=i+1)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=12, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=14,row=i+2)

    window.mainloop()

def viewSec():

    def btnDel():
        window.destroy()
        deleteData.delSecUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateSecDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Section")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields

    ttk.Label(frm, text="Section No:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Section Name:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Section Location:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Manager ID",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)

    lst = connect_exmp.secLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=2, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=i+1)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=4, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=6,row=i+2)

    window.mainloop()

def viewCus():

    def btnDel():
        window.destroy()
        deleteData.delCusUI() 

    def btnUpdate():
        window.destroy()
        updateUi.updateCusDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Customer")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Customer ID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Customer Name:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Phone No:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Mail:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Sex:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)

    lst = connect_exmp.cusLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()

def viewSup():

    def btnDel():
        window.destroy()
        deleteData.delSupUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateSupDio()

    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Supplier")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Supplier ID:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Phone No:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Company:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Address:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Mail:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)

    lst = connect_exmp.supLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=4, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=6, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=8,row=i+2)

    window.mainloop()

def viewClo():

    def btnDel():
        window.destroy()
        deleteData.delCloUI()

    def btnUpdate():
        window.destroy()
        updateUi.updateCloDio()


    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (width,height))
    # window.eval('tk::PlaceWindow . center')

    window.title("View Cloth")

    # frame creation
    frm = ttk.Frame(window,padding=20)
    frm.grid()

    # Fields
    ttk.Label(frm, text="Cloth NO:",padding=10,relief="raised").grid(column=0, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
    ttk.Label(frm, text="Cloth Type:",padding=10,relief="raised").grid(column=2, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
    ttk.Label(frm, text="Cloth Size:",padding=10,relief="raised").grid(column=4, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
    ttk.Label(frm, text="Category:",padding=10,relief="raised").grid(column=6, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
    ttk.Label(frm, text="Company:",padding=10,relief="raised").grid(column=8, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
    ttk.Label(frm, text="Price:",padding=10,relief="raised").grid(column=10, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
    ttk.Label(frm, text="Customer ID:",padding=10,relief="raised").grid(column=12, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
    ttk.Label(frm, text="Supplier ID:",padding=10,relief="raised").grid(column=14, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=15, row=0)
    ttk.Label(frm, text="Section No:",padding=10,relief="raised").grid(column=16, row=0)
    ttk.Label(frm, text="",padding=10).grid(column=17, row=0)

    lst = connect_exmp.cloLst()

    for i in range(len(lst)):
        ttk.Label(frm, text=lst[i][0],padding=10,relief="flat").grid(column=0, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=1, row=0)
        ttk.Label(frm, text=lst[i][1],padding=10,relief="flat").grid(column=2, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=3, row=0)
        ttk.Label(frm, text=lst[i][2],padding=10,relief="flat").grid(column=4, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=5, row=0)
        ttk.Label(frm, text=lst[i][3],padding=10,relief="flat").grid(column=6, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=7, row=0)
        ttk.Label(frm, text=lst[i][4],padding=10,relief="flat").grid(column=8, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=9, row=0)
        ttk.Label(frm, text=lst[i][5],padding=10,relief="flat").grid(column=10, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=11, row=0)
        ttk.Label(frm, text=lst[i][6],padding=10,relief="flat").grid(column=12, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=13, row=0)
        ttk.Label(frm, text=lst[i][7],padding=10,relief="flat").grid(column=14, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=15, row=0)
        ttk.Label(frm, text=lst[i][8],padding=10,relief="flat").grid(column=16, row=i+1)
        # ttk.Label(frm, text="",padding=10).grid(column=17, row=0)
    ttk.Button(frm, text="Update", command=btnUpdate).grid(column=12, row=i+2)
    ttk.Label(frm, text="",padding=10).grid(column=13, row=i+2)
    ttk.Button(frm, text="Delete", command=btnDel).grid(column=14, row=i+2)

    ttk.Button(frm, text="Cancel", command=window.destroy).grid(column=16,row=i+2)

    window.mainloop()