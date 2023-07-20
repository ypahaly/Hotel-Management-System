from tkinter import*
from PIL import Image, ImageTk


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        #=================ist img==========
        img1=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ===============logo===========
        img2=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img2=img2.resize((1550,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #===============title=============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman" , 40 ,"bold"),bg="black",fg="cyan", bd=4, relief =RIDGE)
        lbl_title.place(x=0 ,y=140 ,width=1550, height=50)
        

        #==========mainFrame=============
        main_frame=Frame(self.root,bd=4 , relief=RIDGE)
        main_frame.place(x=0 ,y=190 ,width=1550, height=620)

        #===========menu=================
        lbl_menu=Label(self.root,text="MENU" ,font=("times new roman" ,20,"bold") ,bg="black" ,fg="gold" ,bd=4,relief =RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #==========btn Frame=============
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame, text="CUSTOMER" ,font=("times of new roman" , 14 ,"bold") ,bg="black" ,fg="gold" ,bd=0,cursor="hand1")
        cust_btn.grid(row=0, column=0 , pady=1)

        room_btn=Button(btn_frame, text="CUSTOMER" ,font=("times of new roman" , 14 ,"bold") ,bg="black" ,fg="gold" ,bd=0,cursor="hand2")
        room_btn.grid(row=0, column=0 , pady=1)

        details_btn=Button(btn_frame, text="CUSTOMER" ,font=("times of new roman" , 14 ,"bold") ,bg="black" ,fg="gold" ,bd=0,cursor="hand2")
        details_btn.grid(row=0, column=0 , pady=1)

        report_btn=Button(btn_frame, text="REPORT" ,font=("times of new roman" , 14 ,"bold") ,bg="black" ,fg="gold" ,bd=0,cursor="hand2")
        report_btn.grid(row=0, column=0 , pady=1)

        logout_btn=Button(btn_frame, text="LOGOUT" ,font=("times of new roman" , 14 ,"bold") ,bg="black" ,fg="gold" ,bd=0,cursor="hand2")
        logout_btn.grid(row=0, column=0 , pady=1)
        


        #===============right side image============================

        img3=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        lblimg1=Label(main_frame,image=self.photoimg3 ,bd=4, relief=RIDGE)
        lblimg1.place(x=225 ,y=0, width=1310, height=590)

        #===============down images==============================

        img4=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)


        lblimg1=Label(main_frame,image=self.photoimg4 ,bd=4, relief=RIDGE)
        lblimg1.place(x=0,y=225, width=230, height=210)

        img5=Image.open(r"C:\Users\HP\Desktop\Hotel Management System\hotelimg1.webp")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        lblimg1=Label(main_frame,image=self.photoimg5 ,bd=4, relief=RIDGE)
        lblimg1.place(x=0 ,y=420, width=230, height=190)


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()










































