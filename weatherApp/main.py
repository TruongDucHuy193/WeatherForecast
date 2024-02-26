# from tkinter import *
# import tkinter as tk
# from geopy.geocoders import Nominatim
# from tkinter import ttk,messagebox
# from timezonefinder import TimezoneFinder
# from datetime import *
# import requests
# import pytz
# from PIL import Image, ImageTk

# class weatherApp():
#     def __init__(self, window):
#         self.window = window
#         self.setui()

#     def setui(self):
#         self.create_window()
#         self.create_labels()
#         self.search_bar()
#         self.create_bg()
#         self.set_iconweather()
#         self.thpwv()

#     def create_window(self):
#         self.window.title("Weather forecast")
#         self.window.geometry("800x470+350+200")
#         self.window.resizable(False, False)
#         self.window.configure(bg="#57adff")
#         self.icon = PhotoImage(file="shapes/logo.png")
#         self.window.iconphoto(False, self.icon)

#     def create_labels(self):
#         self.timezone = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
#         self.timezone.place(x=20,y=50)

#         self.clock = Label(self.window, font=("Arial",14,"bold"), fg="white", bg="#57adff")
#         self.clock.place(x=30,y=20)

#     #thông tin thời tiết
#     def thpwv(self):
#         #in nội dung
#         self.label1 = Label(self.window, text="Nhiệt độ", font=("Times New Roman", 13), fg="white", bg="#4169E1")
#         self.label1.place(x=160, y=300)

#         self.label2 = Label(self.window, text="Độ ẩm", font=("Times New Roman", 13), fg="white", bg="#4169E1")
#         self.label2.place(x=260, y=300)

#         self.label3 = Label(self.window, text="Áp suất", font=("Times New Roman", 13), fg="white", bg="#4169E1")
#         self.label3.place(x=360, y=300)

#         self.label4 = Label(self.window, text="Tốc độ gió", font=("Times New Roman", 13), fg="white", bg="#4169E1")
#         self.label4.place(x=460, y=300)

#         self.label5 = Label(self.window, text="Tầm nhìn", font=("Times New Roman", 13), fg="white", bg="#4169E1")
#         self.label5.place(x=570, y=300)

#         #in thông tin
#         self.t = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
#         self.t.place(x=160, y=330)

#         self.h = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
#         self.h.place(x=260, y=330)

#         self.p = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
#         self.p.place(x=360, y=330)

#         self.w = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
#         self.w.place(x=460, y=330)

#         self.v = Label(self.window, font=("Times New Roman", 11), fg="white", bg="#4169E1")
#         self.v.place(x=570, y=330)

#     def create_bg(self):
#         rec = tk.Canvas(self.window, width=500, height=250, bg="#4169E1")  
#         rec.place(relx=0.5, rely=0.5, anchor="center")

#     def search_bar(self):
#         self.textfield = tk.Entry(self.window, width=15, font=("poppins", 25, "bold"), bg="white", border=0, fg="black")
#         self.textfield.place(x=280, y=10)
        
#         self.search_icon = PhotoImage(file="shapes/search.png")
#         self.sear_icon = Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#57adff", command=self.getWeather)
#         self.sear_icon.place(x=550, y=1)

#     def set_iconweather(self):
#         current_time = datetime.now().hour
#         if current_time >= 7 and current_time <= 13:
#             self.icon_wea = PhotoImage(file="iconWeather/01d.png")
#             Label(self.window, image=self.icon_wea, bg="#4169E1").place(x=180, y=130)
    
#     #nhận api
#     def get_api(self):
#         with open("weatherApp/apiKey.txt",'r') as api_file:
#             api_key = api_file.read().strip()
#         return api_key
    
#     #lấy dữ liệu thời tiết
#     def getWeather(self):
#         city = self.textfield.get()
#         geolocator = Nominatim(user_agent="geoapiExcercises")
#         location = geolocator.geocode(city)
#         obj = TimezoneFinder()
#         result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
#         self.timezone.config(text=result)
#         home=pytz.timezone(result)
#         local_time=datetime.now(home)
#         current_time = local_time.strftime("%I:%M %p")
#         self.clock.config(text=current_time)

#         #đường dẫn lấy dữ liệu thời tiết
#         api_key = self.get_api()
#         api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly,daily&appid="+api_key
#         json_data = requests.get(api).json()

#         #current
#         temp = json_data["current"]["temp"]
#         humidity = json_data["current"]["humidity"]
#         pressure = json_data["current"]["pressure"]
#         wind = json_data["current"]["wind_speed"]
#         visibility = json_data["current"]["visibility"]
#         #descripption = json_data["current"]["weather"][0]["description"]
        
#         self.t.config(text=f"{temp} °C")
#         self.h.config(text=f"{humidity} %")
#         self.p.config(text=f"{pressure} mb")
#         self.w.config(text=f"{wind} km/h")
#         self.v.config(text=f"{visibility} km")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = weatherApp(root)
#     root.mainloop()
