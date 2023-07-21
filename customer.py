from tkinter import*
from PIL import Image ,ImageTk #pip install pillow
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1290x550+230+220")


        #===============title=============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("Arial" , 18 ,"bold"),bg="black",fg="cyan", bd=4, relief =RIDGE)
        lbl_title.place(x=0 ,y=0 ,width=1295, height=50)


        # ===============logo===========
        img2=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #==============label Frame=============
        labelframeleft=LabelFrame(self.root ,bd=2 ,relief=RIDGE,text="Customer Details" ,font=("Georgia" ,12 ,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #===============labels and entrys==============
        #custref
        lbl_cust_ref=Label(labelframeleft ,text="Customer Ref:" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lbl_cust_ref.grid(row=0,column=0 ,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold"),width=29)
        enty_ref.grid(row=0,column=1)


        #custname
        cname=Label(labelframeleft , font =("arial" ,12 ,"bold") ,text="Customer Name:" ,padx=2 ,pady=6)
        cname.grid(row=1,column=0 ,sticky=W)

        txtcname=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") , width=29)
        enty_ref.grid(row=1,column=1)

        #mother name

        lblmname=Label(labelframeleft ,text="Mother Name:" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblmname.grid(row=2,column=0 ,sticky=W)

        txtcname=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") ,width=29)
        txtcname.grid(row=2,column=1)
        
        #gender combobox
        label_gender=Label(labelframeleft ,text="Customer Ref" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        label_gender.grid(row=3,column=0 ,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft ,font =("times new roman" ,12 ,"bold"), width=27 ,state=DISABLED)
        combo_gender["value"]=("Male","Female" ,"Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)




        #postcode

        lblPostCode=Label(labelframeleft ,text="Mother Name" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblPostCode.grid(row=4,column=0 ,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") , width=29)
        txtPostCode.grid(row=4,column=1)

        #mobilenumber

        lblMobile=Label(labelframeleft ,text="Mobile Name:" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblMobile.grid(row=5,column=0 ,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") , width=29)
        txtMobile.grid(row=5,column=1)

        #email

        lblEmail=Label(labelframeleft ,text="Email:" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblEmail.grid(row=6,column=0 ,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") ,width=29)
        txtEmail.grid(row=6,column=1)

        #idproofcombobox

        lblNationality=Label(labelframeleft ,text="Nationality" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblNationality.grid(row=7,column=0 ,sticky=W)
        combo_Natonality=ttk.Combobox(labelframeleft ,font =("times new roman" ,12 ,"bold"), width=27 )
        combo_Natonality["value"]=("Aadhar Card","Driving licence" ,"Passport")
        combo_Natonality.current(0)
        combo_Natonality.grid(row=7,column=1)





        #idnumber

        lblEmail=Label(labelframeleft ,text="Email" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblEmail.grid(row=8,column=0 ,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") ,width=29)
        txtEmail.grid(row=8,column=1)

        #address

        lblAddress=Label(labelframeleft ,text="Address:" ,font =("times new roman" ,12 ,"bold") ,padx=2 ,pady=6)
        lblAddress.grid(row=9,column=0 ,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,font=("times new roman" ,12 ,"bold") ,width=29)
        txtAddress.grid(row=9,column=1)

        #===============btns==========
        btn_frame=Frame(labelframeleft ,bd=2 ,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd= Button(btn_frame ,text="Add" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnAdd.grid(row=0,column=0 ,padx=1)

        btnUpdate= Button(btn_frame ,text="Update" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnUpdate.grid(row=0,column=1 ,padx=1)

        btnDelete= Button(btn_frame ,text="Delete" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnDelete.grid(row=0,column=2 ,padx=1)

        btnReset= Button(btn_frame ,text="Reset" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnReset.grid(row=0,column=3 ,padx=1)

        #===================tabel frame================
        Table_Frame=LabelFrame(self.root ,bd=2 ,relief=RIDGE ,text="View Details And Search System" ,font=("arial" ,12, "bold"), padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
        

        lblSearchby=Label( Table_Frame,text="Search By:" ,font =("arial" ,12 ,"bold") ,bg="blue" ,fg="cyan")
        lblSearchby.grid(row=0,column=0 ,sticky=W)

        combo_Search=ttk.Combobox(Table_Frame ,font =("times new roman" ,12 ,"bold"), width=24, state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0 ,column=1)

        txtSearch=ttk.Entry(Table_Frame,font=("arial" ,12 ,"bold") ,width=24)
        txtSearch.grid(row=0,column=2 ,padx=2)

        btnSearch= Button(btn_frame ,text="Search" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnSearch.grid(row=0,column=3 ,padx=1)

        btnShowAll= Button(btn_frame ,text="Show All" , font=("arial" ,11, "bold"),bg="black" ,fg="gold" ,width=10)
        btnShowAll.grid(row=0,column=4 ,padx=1)
        
        #==========Show data Table============

        details_table=Frame(Table_Frame ,bd=2 ,relief=RIDGE)
        details_table.place(x=0,y=400,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table ,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table ,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table ,columns=("ref","name","mother","gender","post","mobile","email",
                                                                     "nationality","idproof","idnumber","address") ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",texts="Ref NO")
        self.Cust_Details_Table.heading("name",texts="Name")
        self.Cust_Details_Table.heading("mother",texts="Mother Name")
        self.Cust_Details_Table.heading("gender",texts="Gender")
        self.Cust_Details_Table.heading("post",texts="PostCode")
        self.Cust_Details_Table.heading("mobile",texts="Mobile")
        self.Cust_Details_Table.heading("email",texts="Email")
        self.Cust_Details_Table.heading("nationality",texts="Nationality")
        self.Cust_Details_Table.heading("id proof",texts="Id Proof")
        self.Cust_Details_Table.heading("idnumber",texts="Id Number")
        self.Cust_Details_Table.heading("address",texts="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        


        



        




if __name__== "__main__":
    root =Tk()
    obj=Cust_Win(root)
    root.mainloop()