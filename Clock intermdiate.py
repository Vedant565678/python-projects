
import json
from re import sub
from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

# brightness
import screen_brightness_control as pct

# Adiuo
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# clock

from time import strftime

# calendar

from tkcalendar import *

# open google

import pyautogui

import subprocess
import webbrowser as wb
import random

app2 = Toplevel()
app2.geometry("850x120+300+10")
app2.resizable(False, False)
app2.title("Clock")
app2.configure(bg='#292e2e')

# clock
image_icon = PhotoImage(file="Image/app2.png")
app2.iconphoto(False, image_icon)

def clock():
    text = strftime("%H:%M:%S %p")
    lbl.config(text=text)
    lbl.after(1000, clock)

lbl = Label(app2, font=("Digital-7", 50, 'bold'),width=20, bg="#f4f5f5", fg="#292e2e")
lbl.pack(anchor=CENTER, pady=20)
clock()
app2.mainloop()
