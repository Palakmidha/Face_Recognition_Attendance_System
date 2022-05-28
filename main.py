from pyclbr import Function
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from tokenize import String
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img=Image.open(r"images\Pic1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

       
        #Second Image 
        img1=Image.open(r"images\Pic3.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        # Third Image  
        img2=Image.open(r"images\Pic2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # Background Image
        img3=Image.open(r"images\Pic4.jpg")
        img3=img3.resize((1537,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",32,"bold"),bg="#97C4B8",fg="black")
        title_lbl.place(x=0,y=0,width=1500,height=60)


        #Time
        def time():
             string=strftime('%H:%M:%S %p')    
             lbl.config(text=string)
             lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="#97C4B8",foreground="black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # Student/Employee Button
        img4=Image.open(r"images\Pic5.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.Student_details,cursor="hand2")
        b1.place(x=200,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Student/Employee Details",command=self.Student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=200,y=250,width=180,height=35)


        # Detect Face Button
        img5=Image.open(r"images\Pic7.png")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=600,y=250,width=180,height=35)


        # Attendance Button
        img6=Image.open(r"images\Pic8.png")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1000,y=100,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=1000,y=250,width=180,height=35)

        


        # Train Face Button
        img8=Image.open(r"images\Pic6.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.tain_data)
        b1.place(x=200,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.tain_data,font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=200,y=500,width=180,height=35)

        
        # Photos Button
        img9=Image.open(r"images\Pic12.jpg")
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=600,y=500,width=180,height=35)


        


        # Exit Button
        img11=Image.open(r"images\Pic11.png")
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=350,width=180,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=1000,y=500,width=180,height=35)


    def open_img(self):
        os.startfile("data") 

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to Exit this project?",parent=self.root)      
         if self.iExit>0:
              self.root.destroy()
         else:
              return


        # Function Buttons

    def Student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)


    def tain_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)     


    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window) 



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
