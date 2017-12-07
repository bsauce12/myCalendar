from tkinter import *
import tkinter as tk #allows for me to reference tkinter as tk
import random
from tkinter.ttk import * #imports all functions for tkinter.ttk class
from subprocess import call #importing the method call
import calendar
from datetime import datetime
import ctypes
import csv
#import tkMessageBox

#creating variables that allow me to change fonts
titlefont = ("Courier New", 22, "bold")
paragraphfont = ("Times New Roman", 16)
subtitlefont = ("Courier New", 12)

class Main(tk.Frame):
    #pass (this is a holder)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent) #lets me view the page
        self.controller = controller # reference controller without using "self."
        #tkLabel lets you create text
        #self.title = tk.Label(self, text = "My Calender", font = titlefont)
        #self.title.pack(side = "top", fill = "x", pady = 10)
        self.title = tk.Label(self, text = "Welcome To MyCalendar", font = titlefont)
        self.title.pack(side='top', fill ='x', pady=10)
        self.select = tk.Label(self, text = "Please Select form the options below", font=paragraphfont)
        self.select.pack(side="top", fill="x")
        self.book = tk.Label(self, text = "", font = titlefont)
        self.book.pack(side="top", fill="x")
        self.MCButton = tk.Button(self,text="My Calendar",bg ="black", fg = "white",command=lambda: controller.show_frame("MyCalendar"))
        self.MCButton.pack()
        self.RMButton = tk.Button(self,text="Reminder",bg ="black", fg = "white",command=lambda: controller.show_frame("Reminder"))
        self.RMButton.pack()
        self.FMButton = tk.Button(self,text="Form",bg ="black", fg = "white",command=lambda: controller.show_frame("Form"))
        self.FMButton.pack()
        self.AUButton = tk.Button(self,text="About the App",bg ="black", fg = "white",command=lambda: controller.show_frame("Aboutus"))
        self.AUButton.pack()
class Reminder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.title1 = tk.Label(self, text = "Reminders", font = titlefont)
        self.title1.pack(side = "top",fill ="x", pady = 10)
        self.welcome = tk.Label(self, text = "Please enter a date and time with", font=paragraphfont)
        self.welcome.pack(side ="top" , fill ="x")
        self.welcome1 = tk.Label(self, text = "A brief discription of what your event is.", font = paragraphfont)
        self.welcome1.pack(side = "top", fill = "x")
        
        self.Time = StringVar ()
        self.Date = StringVar()
        self.Discription = StringVar()
        
        label1 = tk.Label(self, text="Date:")
        label1.pack()
        e1 = Entry(self, textvariable=self.Date)
        e1.pack()

        label2 = tk.Label(self, text="Time:")
        label2.pack()

        e2 = Entry(self,textvariable = self.Time)
        e2.pack()

        label3 = tk.Label(self, text="Discription:")
        label3.pack()

        e3 = Entry(self,textvariable = self.Discription)
        e3.pack()

        self.BCButton = tk.Button(self,text="Back",font = titlefont,bg ="black", fg = "white",command=lambda: controller.show_frame("Main"))
        self.BCButton.pack(side = "bottom")
        button = Button(self, text="Save",command=lambda: self.save())
        button.pack()
  #      self.saveButton = tk.Button(self,text="Save",font = paragraphfont,bg ="black", fg = "white",command=lambda: controller.show_frame("Main"))
 #       self.saveButton.pack()
        

class MyCalendar(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label1 = tk.Label(self, text="Year:")
        label1.pack()
        self.Year = StringVar ()
        self.Month = StringVar()
        e1 = Entry(self, textvariable=self.Year)
        e1.pack()

        label2 = tk.Label(self, text="Month:")
        label2.pack()

        e2 = Entry(self,textvariable = self.Month)
        e2.pack()

        button = Button(self, text="Show",command=lambda: self.cal())
        button.pack()
        self.BCButton = tk.Button(self,text="Back",font = titlefont,bg ="black", fg = "white",command=lambda: controller.show_frame("Main"))
        self.BCButton.pack(side = "bottom")

    def cal(self):
        y = self.Year.get()
        m = self.Month.get()
        cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
        print (cal_x)
        cal_out = tk.Label(self, text=cal_x, font=('courier', 12, 'bold'), justify = LEFT, bg='lightblue')
        cal_out.pack(padx=3, pady=10, expand=True)
class Form(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.title1 = tk.Label(self, text = "Form", font = titlefont)
        self.title1.pack(side = "top",fill ="x", pady = 10)
        self.welcome = tk.Label(self, text = "Please Feel free to leave your", font=paragraphfont)
        self.welcome.pack(side ="top" , fill ="x")
        self.welcome1 = tk.Label(self, text = "comments/concerns here!", font = paragraphfont)
        self.welcome1.pack(side = "top", fill = "x")
        
        self.comment = StringVar ()
        
        label1 = tk.Label(self, text="Comments/Concerns:")
        label1.pack()
        e1 = Entry(self, textvariable=self.comment)
        e1.pack()
        print(e1)


        self.BCButton = tk.Button(self,text="Back",font = titlefont,bg ="black", fg = "white",command=lambda: controller.show_frame("Main"))
        self.BCButton.pack(side = "bottom")
        
        
    def cal(self):
        y = self.comment.get()

        print (y)
        save_out = tk.Label(self, text=cal_x, font=('courier', 12, 'bold'), justify = LEFT, bg='lightblue')
        save_out.pack(padx=3, pady=10, expand=True)
 
    def retrieve_input():
        inputValue = tk.textBox.get("1.0","end-1c")
        print(inputValue)

        textBox=Text(root, height=2, width=10)
        textBox.pack()
        buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
        buttonCommit.pack()
        
   # def writeToFile(self):
        #with open('WorkOrderLog.csv', 'a') as f:
 #           w=csv.writer(f, quoting=csv.QUOTE_ALL)
 #           w.writerow([self.e.get()])
class Aboutus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.title1 = tk.Label(self, text = "Here's A little about the app", font = titlefont)
        self.title1.pack(side = "top",fill ="x", pady = 10)
        self.welcome = tk.Label(self, text = "Ever Had a problem remebering things constantly?", font=paragraphfont)
        self.welcome.pack(side ="top" , fill ="x")
        self.welcome1 = tk.Label(self, text = "Then MyCalendar is just right for you.", font = paragraphfont)
        self.welcome2 = tk.Label(self, text = "This app is simple little calendar generator", font = paragraphfont)
        self.welcome2.pack(side = "top" , fill = "x")
        self.welcome3 = tk.Label(self, text = "that was made with the forgetful (such as myself) in mind.", font=paragraphfont)
        self.welcome3.pack(side = "top" , fill = "x")

        self.BCButton = tk.Button(self,text="Back",font = titlefont,bg ="black", fg = "white",command=lambda: controller.show_frame("Main"))
        self.BCButton.pack(side = "bottom")
#Creating the application

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        #self allows you to call any variable or function in the class
        #*args allows you to use single dimension lists
        #**kwargs allows you to use multi dimension lists
        #niether are needed but both are common in all init functions
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("My Calendar") #creating the title of the app
        self.geometry("600x600+250+50") #makes a standard size for the main app
        #creating a container
        container = tk.Frame(self)
        #pack allows you to to tell tk inter how to pack things;
        #expand is true if you increase the size of the application
        #everything expands with it
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (Main, MyCalendar, Reminder,Form,Aboutus):
            page_name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Main")


        btn_exit = tk.Button(self, text = "Exit", fg = "black", bg = "white", command = exit, font=titlefont)
        btn_exit.pack()

    #runs the frame from above
    def show_frame(self, pagename):
        #shows a frame for the given page name
        frame = self.frames[pagename]
        frame.tkraise()

if __name__=="__main__":
    root = App() #runs the app
    root.mainloop() #lets the app run forever until user quits

        

