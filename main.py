import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os
import requests

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        result = (
            f"{'-' * 40}\n"
            f"Weather in {data['name']}, {data['sys']['country']}:\n"
            f"Temperature: {data['main']['temp']}°C\n"
            f"Feels Like: {data['main']['feels_like']}°C\n"
            f"Condition: {data['weather'][0]['description'].title()}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind: {data['wind']['speed']} m/s\n"
            f"{'-' * 40}"
        )
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# build tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
