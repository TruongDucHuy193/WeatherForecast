from tkinter import *
import tkinter as tk
# from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from datetime import *
from datetime import datetime
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
        self.create_day_wea_box()
        self.thpwv()

    def create_window(self):
        self.window.title("Weather forecast")
        self.window.geometry("890x470+350+200")
        self.window.resizable(False, False)
        self.window.configure(bg="#57adff")
        self.icon = PhotoImage(file="shapes/logo.png")
        self.window.iconphoto(False, self.icon)


    def create_labels(self):
        self.timezone_label = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
        self.timezone_label.place(x=30,y=50)

        self.clock = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
        self.clock.place(x=30,y=20)


    #thông tin thời tiết
    def thpwv(self):
        #in nội dung
        self.label2 = Label(self.window, text="Độ ẩm", font=("Arial", 13), fg="white",bg="#57adff")
        self.label2.place(x=500, y=120)

        self.label3 = Label(self.window, text="Áp suất", font=("Ariel", 13), fg="white",bg="#57adff")
        self.label3.place(x=500, y=145)

        self.label4 = Label(self.window, text="Tốc độ gió", font=("Ariel", 13), fg="white",bg="#57adff")
        self.label4.place(x=500, y=170)

        self.label5 = Label(self.window, text="Tầm nhìn", font=("Ariel", 13), fg="white",bg="#57adff")
        self.label5.place(x=500, y=195)

        #in thông tin
        self.t = Label(self.window, font=("Ariel", 30,"bold"), fg="white",bg="#57adff")
        self.t.place(x=150, y=120)

        self.h = Label(self.window, font=("Ariel", 13), fg="white",bg="#57adff")
        self.h.place(x=600, y=120)

        self.p = Label(self.window, font=("Ariel", 13), fg="white",bg="#57adff")
        self.p.place(x=600, y=145)

        self.w = Label(self.window, font=("Ariel", 13), fg="white",bg="#57adff")
        self.w.place(x=600, y=170)

        self.v = Label(self.window, font=("Ariel", 13), fg="white",bg="#57adff")
        self.v.place(x=600, y=195)

        self.timezone_label.config(text=".../.....")
        self.t.config(text="... °C")
        self.h.config(text="... %")
        self.p.config(text="... mb")
        self.w.config(text="... km/h")
        self.v.config(text="... km")
        
    

    def search_bar(self):
        self.textfield = tk.Entry(self.window, width=15, font=("poppins", 25, "bold"), bg="white", border=0, fg="black")
        self.textfield.place(x=280, y=10)
        self.textfield.insert(0, "Loading...")
        t1 = Thread(target=self.thread_get_current_local, args=(self, ))
        t1.start()

        self.search_icon = PhotoImage(file="shapes/search.png")
        self.sear_icon = Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#57adff", command=self.thread_set_weather)
        self.sear_icon.place(x=550, y=1)
    
    def create_day_wea_box(self):
        self.firstbox = PhotoImage(file="shapes/Rounded Rectangle 2.png")
        self.secondbox = PhotoImage(file="shapes/Rounded Rectangle 2 copy.png")
        x = [300, 400, 500, 600, 700, 800]


        frame = Frame(self.window, bg="#212120")
        frame.place(x=30, y=320)

        Label(frame, image=self.firstbox).pack(side=LEFT)

        for i in range(len(x)):
            frames = Frame(self.window, bg="#212120")
            frames.place(x=x[i], y=330)
            Label(frames, image=self.secondbox).pack(side=LEFT)

        # frame2 = Frame(self.window, bg="#212120")
        # frame2.place(x=300, y=330)

        # Label(frame2, image=self.secondbox).pack(side=LEFT)

        # frame3 = Frame(self.window, bg="#212120")
        # frame3.place(x=400, y=330)

        # Label(frame3, image=self.secondbox).pack(side=LEFT)

        # frame4 = Frame(self.window, bg="#212120")
        # frame4.place(x=500, y=330)

        # Label(frame4, image=self.secondbox).pack(side=LEFT)

        # frame5 = Frame(self.window, bg="#212120")
        # frame5.place(x=600, y=330)

        # Label(frame5, image=self.secondbox).pack(side=LEFT)

        # frame6 = Frame(self.window, bg="#212120")
        # frame6.place(x=700, y=330)

        # Label(frame6, image=self.secondbox).pack(side=LEFT)

        # frame7 = Frame(self.window, bg="#212120")
        # frame7.place(x=800, y=330)

        # Label(frame7, image=self.secondbox).pack(side=LEFT)


        self.day1=Label(frame,font="arial 20",borderwidth=0)
        self.day1.place(x=80,y=5)

        first = datetime.now()
        self.day1.config(text = first.strftime("%A"))
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
        self.set_iconweather(description)

    def set_iconweather(self, description):
        current_time = datetime.now().hour
        gr_11d = ["thunderstorm with light rain","thunderstorm with rain","thunderstorm with heavy rain","light thunderstorm","thunderstorm","heavy thunderstorm","ragged thunderstorm","thunderstorm with light drizzle","thunderstorm with drizzle","thunderstorm with heavy drizzle"]
        gr_9d = ["light intensity drizzle","drizzle","heavy intensity drizzle","light intensity drizzle rain","rain","heavy intensity drizzle rain","shower rain and drizzle","heavy shower rain and drizzle","shower drizzle","light intensity shower rain","shower rain","heavy intensity shower rain","ragged shower rain"]
        gr_10d = ["light rain","moderate rain","heavy intensity rain","very heavy rain","extreme rain"]
        gr_13d = ["light snow","snow","heavy snow","sleet","light shower sleet","shower sleet","light rain and snow","rain and snow","light shower snow","shower snow","heavy shower snow","freezing rain"]
        gr_50d = ["mist","smoke","haze","sand/dust whirls","fog","sand","dust","volcanic ash","squalls","tornado"]
        gr_clouds = ["broken clouds","overcast clouds"]
        if current_time in range(6,18):
            if description=="clear sky":
                self.icon_wea = PhotoImage(file="iconWeather/01d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)
            
            elif description=="few clouds":
                self.icon_wea = PhotoImage(file="iconWeather/02d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description=="scattered clouds":
                self.icon_wea = PhotoImage(file="iconWeather/03d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)
            
            elif description in list(gr_clouds):
                self.icon_wea = PhotoImage(file="iconWeather/04d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description in list(gr_9d):
                self.icon_wea = PhotoImage(file="iconWeather/09d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description in list(gr_10d):
                self.icon_wea = PhotoImage(file="iconWeather/10d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)


            elif description in list(gr_11d):
                self.icon_wea = PhotoImage(file="iconWeather/11d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description in list(gr_13d):
                self.icon_wea = PhotoImage(file="iconWeather/13d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)


            elif description in list(gr_50d):
                self.icon_wea = PhotoImage(file="iconWeather/50d.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

        else:
            if description=="clear sky":
                self.icon_wea = PhotoImage(file="iconWeather/01n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)
            
            elif description=="few clouds":
                self.icon_wea = PhotoImage(file="iconWeather/02n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description=="scattered clouds":
                self.icon_wea = PhotoImage(file="iconWeather/03n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)
            
            elif description in list(gr_clouds):
                self.icon_wea = PhotoImage(file="iconWeather/04n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description=="shower rain":
                self.icon_wea = PhotoImage(file="iconWeather/09n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description=="rain":
                self.icon_wea = PhotoImage(file="iconWeather/10n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)


            elif description=="thunderstorm":
                self.icon_wea = PhotoImage(file="iconWeather/11n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)

            elif description=="snow":
                self.icon_wea = PhotoImage(file="iconWeather/13n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)


            elif description=="mist":
                self.icon_wea = PhotoImage(file="iconWeather/50n.png")
                Label(self.window, image=self.icon_wea, bg="#57adff").place(x=40, y=90)