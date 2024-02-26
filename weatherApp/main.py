from tkinter import *
import tkinter as tk

from GUI import weatherApp
from apiWeather import get_api

KEY_API= get_api()

if __name__ == "__main__":
    root = tk.Tk()
    app = weatherApp(root, KEY_API)
    root.mainloop()