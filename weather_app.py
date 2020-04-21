import tkinter as tk
from tkinter import font
import requests

canvas_height = 500
canvas_width = 600

# def format_response(weather): 
#     name = weather['name']
#     desc = weather['weather'][0]['description']
#     temp = weather['main']['temp']
 
#     return str(name) + ' \n' + str(desc) + ' \n' + str(temp)

def format_response(weather): 
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature %i°C' % (name, desc, temp)
    except:
        final_str = 'Cannot retrieve that information'

    return final_str

def get_weather(city):
    weather_key = '2109bb73b0ea1e4fd9ebb4210d08663e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# 2109bb73b0ea1e4fd9ebb4210d08663e

root = tk.Tk()

# main canvas
canvas = tk.Canvas(root, height=canvas_height, width=canvas_width)
canvas.pack()
bg_image = tk.PhotoImage(file="landscape.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# upper frame
frame = tk.Frame(root, bg="#03fcdb", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 12))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower Frame
lower_frame = tk.Frame(root, bg="#03fcdb", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relwidth=1, relheight=1)






# main loop -- runs the program
root.mainloop()