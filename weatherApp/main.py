import requests
import tkinter as tk

api_key = "3ccf3d4ca0a1d65e4b12c25cd75314d3"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return None

    weather_info = {
        "city": data['name'],
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
    }

    return weather_info

def main():
    city = entry.get()
    weather_info = get_weather(city)

    if weather_info:
        output.config(text=f"City: {weather_info['city']}\nTemperature: {weather_info['temperature']}\nDescription: {weather_info['description']}\nHumidity: {weather_info['humidity']}\nWind Speed: {weather_info['wind_speed']}")
    else:
        output.config(text="Invalid city name")

root = tk.Tk()
root.title = "Weather App"
root.geometry("200x200")  # Set the window size
root.resizable(False, False)  # Make the window not resizable


frame = tk.Frame(root)
frame.pack(padx=0, pady=0)

label = tk.Label(frame, text="Enter city name")
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Get Weather", command=lambda: main())
button.pack()

output = tk.Label(frame)
output.pack(pady=10)

root.mainloop()