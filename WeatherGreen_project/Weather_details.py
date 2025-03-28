import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("800x500+300+100")
        self.root.resizable(False, False)

        # Set icon
        try:
            icon_image = tk.PhotoImage(file="weather-icon.png")
            self.root.iconphoto(False, icon_image)
        except Exception as e:
            print(f"Error loading icon: {e}")

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Search Box
        search_image = tk.PhotoImage(file="Copy of search.png")
        self.myimage = tk.Label(self.root, image=search_image)
        self.myimage.image = search_image
        self.myimage.place(x=20, y=20)

        self.textfield = tk.Entry(self.root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
        self.textfield.place(x=50, y=40)
        self.textfield.focus()

        search_icon = tk.PhotoImage(file="Copy of search_icon.png")
        self.search_button = tk.Button(self.root, image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=self.get_weather)
        self.search_button.image = search_icon
        self.search_button.place(x=400, y=34)

        # Logo
        logo_image = tk.PhotoImage(file="Copy of logo.png")
        self.logo = tk.Label(self.root, image=logo_image)
        self.logo.image = logo_image
        self.logo.place(x=150, y=100)

        # Bottom Box
        frame_image = tk.PhotoImage(file="Copy of box.png")
        self.frame = tk.Label(self.root, image=frame_image)
        self.frame.image = frame_image
        self.frame.pack(padx=5, pady=5, side=tk.BOTTOM)

        # Labels
        self.name = tk.Label(self.root, font=("arial", 15, "bold"))
        self.name.place(x=30, y=100)

        self.clock = tk.Label(self.root, font=("Helvetica", 20))
        self.clock.place(x=30, y=130)

        self.create_labels()

        # Weather data fields
        self.t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
        self.t.place(x=400, y=150)

        self.c = tk.Label(font=("arial", 15, "bold"))
        self.c.place(x=400, y=250)

        self.w = tk.Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.w.place(x=120, y=430)

        self.h = tk.Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.h.place(x=280, y=430)

        self.d = tk.Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.d.place(x=430, y=430)

        self.p = tk.Label(text="....", font=("arial", 20, "bold"), bg="#1ab5ef")
        self.p.place(x=640, y=430)

        # Buttons
        self.forecast_button = tk.Button(self.root, text="Show Forecast", font=("arial", 15, "bold"), command=self.show_forecast, bg="darkred", fg="black")
        self.forecast_button.place(x=620, y=80)

        self.stop_button = tk.Button(self.root, text="Exit", font=("arial", 13, "bold"), command=self.root.destroy, bg="red", fg="black")
        self.stop_button.place(x=700, y=20)

    def create_labels(self):
        labels = [
            ("WIND", 120),
            ("HUMIDITY", 250),
            ("DESCRIPTION", 430),
            ("PRESSURE", 630),
        ]

        colors = ["red", "pink", "yellow", "green"]

        for (text, x), color in zip(labels, colors):
            label = tk.Label(self.root, text=text, font=("Helvetica", 15, "bold"), fg=color, bg="#1ab5ef")
            label.place(x=x, y=400)

    def get_weather(self):
        try:
            city = self.textfield.get()

            geolocator = Nominatim(user_agent="geoapiExercise")
            location = geolocator.geocode(city)

            if not location:
                raise ValueError("Invalid city name")

            obj = TimezoneFinder()
            timezone = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(timezone)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")

            self.clock.config(text=current_time)
            self.name.config(text="CURRENT WEATHER")

            api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=40a6b2df2ecb2023200d9d28215cf41b"
            json_data = requests.get(api).json()

            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            self.t.config(text=f"{temp}°")
            self.c.config(text=f"{condition} | FEELS LIKE {temp}°")

            self.w.config(text=f"{wind} m/s")
            self.h.config(text=f"{humidity} %")
            self.d.config(text=description.capitalize())
            self.p.config(text=f"{pressure} hPa")

        except Exception as e:
            messagebox.showerror("Weather App", "Invalid city name")

    def show_forecast(self):
        try:
            city = self.textfield.get()
            api_key = "6f5c0aa10215c1567d00a306a2309679"
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
            response = requests.get(forecast_url)
            forecast_data = response.json()

            forecast_window = tk.Toplevel(self.root)
            forecast_window.title(f"{city} 5-Day Forecast")
            forecast_window.geometry("800x500+300+100")
            forecast_window.config(bg="#ADD8E6")

            forecast_text = tk.Text(forecast_window, wrap=tk.WORD, bg="lightblue", fg="black", font=("Arial", 14))
            forecast_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            day_count = 1
            last_date = None

            for entry in forecast_data['list']:
                date = datetime.fromtimestamp(entry['dt'])
                if date.hour == 12 and (last_date is None or last_date.date() != date.date()):
                    last_date = date
                    date_str = date.strftime("%A, %B %d")
                    condition = entry['weather'][0]['main']
                    description = entry['weather'][0]['description']
                    temp_min = int(entry['main']['temp_min'] - 273.15)
                    temp_max = int(entry['main']['temp_max'] - 273.15)

                    forecast_str = f"Day {day_count}: {date_str}\nCondition: {condition} ({description.capitalize()})\nTemperature: {temp_min}°C - {temp_max}°C\n\n"

                    forecast_text.insert(tk.END, forecast_str)
                    day_count += 1

        except Exception as e:
            messagebox.showerror("Weather App", "Error retrieving forecast data")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
