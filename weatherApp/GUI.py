from tkinter import *
import tkinter as tk
# from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from datetime import *
from threading import *
import requests
# import pytz
from PIL import Image, ImageTk
from apiWeather import get_weather
from utils import get_current_local
class weatherApp():
    def __init__(self, window, KEY_API):
        self.key_api= KEY_API
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
        self.timezone_label = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
        self.timezone_label.place(x=20,y=50)

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
        self.t = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.t.place(x=160, y=330)

        self.h = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.h.place(x=260, y=330)

        self.p = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.p.place(x=360, y=330)

        self.w = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.w.place(x=460, y=330)

        self.v = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
        self.v.place(x=570, y=330)

        self.timezone_label.config(text=".../.....")
        self.t.config(text="... °C")
        self.h.config(text="... %")
        self.p.config(text="... mb")
        self.w.config(text="... km/h")
        self.v.config(text="... km")
    def create_bg(self):
        rec = tk.Canvas(self.window, width=500, height=250, bg="#4169E1")  
        rec.place(relx=0.5, rely=0.5, anchor="center")

    def search_bar(self):
        self.textfield = tk.Entry(self.window, width=15, font=("poppins", 25, "bold"), bg="white", border=0, fg="black")
        self.textfield.place(x=280, y=10)
        self.textfield.insert(0, "Loading...")
        t1 = Thread(target=self.thread_get_current_local, args=(self, ))
        t1.start()

        self.search_icon = PhotoImage(file="shapes/search.png")
        self.sear_icon = Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#57adff", command=self.thread_set_weather)
        self.sear_icon.place(x=550, y=1)
    
    def thread_get_current_local(self, app_instance):
        city = get_current_local()
        app_instance.textfield.delete(0, END)
        app_instance.textfield.insert(0, city)
        self.set_weather(app_instance)

    def thread_set_weather(self):
        self.timezone_label.config(text=".../.....")
        self.t.config(text="... °C")
        self.h.config(text="... %")
        self.p.config(text="... mb")
        self.w.config(text="... km/h")
        self.v.config(text="... km")
        t1 = Thread(target=(self.set_weather) , args=(self, ))
        t1.start()

    def set_weather(self, app_instance):
        city = app_instance.textfield.get()
        weather = get_weather(self.key_api, city)
        temp, temp_max, temp_min, humidity, pressure, wind, visibility, description, timezone_result = weather[0][0]
        week_day, day, times = weather[0][1]

        app_instance.timezone_label.config(text=timezone_result)
        app_instance.t.config(text=f"{temp} °C")
        app_instance.h.config(text=f"{humidity} %")
        app_instance.p.config(text=f"{pressure} mb")
        app_instance.w.config(text=f"{wind} km/h")
        app_instance.v.config(text=f"{visibility} km")

    def set_iconweather(self):
        current_time = datetime.now().hour
        if current_time >= 7 and current_time <= 13:
            self.icon_wea = PhotoImage(file="iconWeather/01d.png")
            Label(self.window, image=self.icon_wea, bg="#4169E1").place(x=180, y=130)
    