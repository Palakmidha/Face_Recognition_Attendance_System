from ast import Try
from distutils.fancy_getopt import fancy_getopt
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from numpy import mintypecode
import os
import numpy as  np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",32,"bold"),bg="#97C4B8",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=50)

        img_top=Image.open(r"images\Pic18.jpg")
        img_top=img_top.resize((1400,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1400,height=325)

        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="#069A8E",fg="white")
        b1_1.place(x=0,y=370,width=1400,height=60)

        img_bottom=Image.open(r"images\Pic19.jpg")
        img_bottom=img_bottom.resize((1400,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=430,width=1400,height=300)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  

        faces=[]
        ids=[]
    
        for image in path:
            img=Image.open(image).convert('L')      # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        


        ########## Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datsets completed")   



        






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()