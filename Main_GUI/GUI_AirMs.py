from tkinter import *
import webbrowser
parentwindow=Tk()
parentwindow.geometry("1000x666")
parentwindow.title("AirMs Services")



photo = PhotoImage(file = "4.gif")


w = Label(parentwindow, image=photo)
w.pack()


def open1():
    webbrowser.open("https://colab.research.google.com/drive/1GL8dKCfQFYfbOIxPAAiuD0Nsd_rqJON7")

button1=Button(parentwindow,width=20,font=("arial",15),text="Data Wrangling",command=open1)
button1.place(x=180,y=150)

def open2():
    webbrowser.open("https://colab.research.google.com/drive/1X7mbLr7KwipnELSERgyIJlYhSnVpe5YI")

button2=Button(parentwindow,width=20,font=("arial",15),text="Exploratory Analysis",command=open2)
button2.place(x=180,y=250)

def open3():
    webbrowser.open("https://colab.research.google.com/drive/1huqJJ62irYSYB7g55LvhLe013UP7mUO_")

button3=Button(parentwindow,width=20,font=("arial",15),text="Binary Classification",command=open3)
button3.place(x=180,y=350)


def open4():
    webbrowser.open("https://colab.research.google.com/drive/10TXHJBQpNhmGI7tnghwUwPbMc1JjA0-d")
    
button4=Button(parentwindow,width=20,font=("arial",15),text="Multi-class Classification",command=open4)
button4.place(x=180,y=450)


def open5():
    webbrowser.open("https://colab.research.google.com/drive/1PB3YVef1fjOAzZqjgFB2zqICqwvMRXQm")
    
button5=Button(parentwindow,width=20,font=("arial",15),text="Regression TTF",command=open5)
button5.place(x=180,y=550)

def open6():
    webbrowser.open("https://manthannd.github.io/")
    
button6=Button(parentwindow,width=20,font=("arial",15),text="Reach Us",command=open6)
button6.place(x=670,y=620)


parentwindow.mainloop()
