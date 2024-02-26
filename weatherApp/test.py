from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

class weatherApp():
    def __init__(self, window):
        self.window = window
        self.setui()

    def setui(self):
        self.create_window()
        self.create_labels()
        self.search_bar()
        self.create_bg()
        self.set_iconweather()
        self.thpwv()

    def create_window(self):
        self.window.title("Weather forecast")
        self.window.geometry("800x470+350+200")
        self.window.resizable(False, False)
        self.window.configure(bg="#57adff")
        self.icon = PhotoImage(file="shapes/logo.png")
        self.window.iconphoto(False, self.icon)

    def create_labels(self):
        self.timezone = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
        self.timezone.place(x=20,y=50)

        self.clock = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
        self.clock.place(x=30,y=20)

    #thông tin thời tiết
    def thpwv(self):
        #in nội dung
        self.label1 = Label(self.window, text="Nhiệt độ", font=("Times New Roman", 13), fg="white", bg="#4169E1")
        self.label1.place(x=160, y=300)

        self.label2 = Label(self.window, text="Độ ẩm", font=("Times New Roman", 13), fg="white", bg="#4169E1")
        self.label2.place(x=260, y=300)

        self.label3 = Label(self.window, text="Áp suất", font=("Times New Roman", 13), fg="white", bg="#4169E1")
        self.label3.place(x=360, y=300)

        self.label4 = Label(self.window, text="Tốc độ gió", font=("Times New Roman", 13), fg="white", bg="#4169E1")
        self.label4.place(x=460, y=300)

        self.label5 = Label(self.window, text="Tầm nhìn", font=("Times New Roman", 13), fg="white", bg="#4169E1")
        self.label5.place(x=570, y=300)

        #in thông tin
        self.t = Label(self.window, font=("Times New Roman", 24,"bold"), fg="white", bg="#4169E1")
        self.t.place(x=180, y=210)

        self.h = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.h.place(x=260, y=330)

        self.p = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.p.place(x=360, y=330)

        self.w = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.w.place(x=460, y=330)

        self.v = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.v.place(x=570, y=330)

    def create_bg(self):
        rec = tk.Canvas(self.window, width=500, height=250, bg="#4169E1")  
        rec.place(relx=0.5, rely=0.5, anchor="center")

    def search_bar(self):
        self.textfield = tk.Entry(self.window, width=15, font=("poppins", 25, "bold"), bg="white", border=0, fg="black")
        self.textfield.place(x=280, y=10)
        
        self.search_icon = PhotoImage(file="shapes/search.png")
        self.sear_icon = Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#57adff", command=self.getWeather)
        self.sear_icon.place(x=550, y=1)

    def set_iconweather(self):
        current_time = datetime.now().hour
        if current_time >= 7 and current_time <= 24:
            self.icon_wea = PhotoImage(file="iconWeather/01d.png")
            Label(self.window, image=self.icon_wea, bg="#4169E1").place(x=170, y=130)
    
    


if __name__ == "__main__":
    root = tk.Tk()
    app = weatherApp(root)
    root.mainloop()
