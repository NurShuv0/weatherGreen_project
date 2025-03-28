from tkinter import *
from tkinter import ttk, messagebox
import subprocess
import os
from PIL import Image, ImageTk

class TreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WEATHER GREEN APP")
        self.root.geometry("800x500+300+100")
        self.root.resizable(False, False)
        self.root.config(bg="lightblue")

        # Icon
        try:
            self.icon_image = PhotoImage(file="weather-icon.png")
            self.root.iconphoto(False, self.icon_image)
        except Exception as e:
            messagebox.showwarning("Warning", f"Icon not found: {e}")

        # Complete tree data
        self.trees = [
    {"name": "Mango", "seedPrice": 50.0, "season": "Monsoon (June to August)", "category": "Fruit Plant"},
    {"name": "Banana", "seedPrice": 10.0, "season": "Year-round (Best in rainy season)", "category": "Fruit Plant"},
    {"name": "Papaya", "seedPrice": 5.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Guava", "seedPrice": 10.0, "season": "Monsoon Season", "category": "Fruit Plant"},
    {"name": "Jackfruit", "seedPrice": 20.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Litchi", "seedPrice": 50.0, "season": "Winter (November to February)", "category": "Fruit Plant"},
    {"name": "Pineapple", "seedPrice": 20.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Lemon", "seedPrice": 10.0, "season": "Monsoon Season", "category": "Fruit Plant"},
    {"name": "Pomegranate", "seedPrice": 30.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Sapodilla", "seedPrice": 20.0, "season": "Monsoon Season", "category": "Fruit Plant"},
    {"name": "Olive", "seedPrice": 100.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Custard Apple", "seedPrice": 10.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Coconut", "seedPrice": 30.0, "season": "Monsoon Season", "category": "Fruit Plant"},
    {"name": "Starfruit", "seedPrice": 10.0, "season": "Rainy Season", "category": "Fruit Plant"},
    {"name": "Cashew", "seedPrice": 30.0, "season": "Monsoon Season", "category": "Fruit Plant"},
    {"name": "Krishnachura", "seedPrice": 20.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Sheuli", "seedPrice": 10.0, "season": "Year-round", "category": "Flower Plant"},
    {"name": "Radhachura", "seedPrice": 15.0, "season": "Spring (February to April)", "category": "Flower Plant"},
    {"name": "Kanchan", "seedPrice": 20.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Jarul", "seedPrice": 10.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Kadam", "seedPrice": 10.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Shimul", "seedPrice": 15.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Palash", "seedPrice": 10.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Guloncho", "seedPrice": 10.0, "season": "Year-round", "category": "Flower Plant"},
    {"name": "Bokul", "seedPrice": 10.0, "season": "Year-round", "category": "Flower Plant"},
    {"name": "Ratnagiri", "seedPrice": 10.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Sada-Chapa", "seedPrice": 20.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Chandni", "seedPrice": 20.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Akondo", "seedPrice": 10.0, "season": "Year-round", "category": "Flower Plant"},
    {"name": "Champa", "seedPrice": 10.0, "season": "Year-round", "category": "Flower Plant"},
    {"name": "Kodom", "seedPrice": 10.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Madhabilata", "seedPrice": 20.0, "season": "Spring (March to April)", "category": "Flower Plant"},
    {"name": "Brinjal", "seedPrice": 20.0, "season": "Late winter to early spring (December to February)", "category": "Vegetable Plant"},
    {"name": "Tomato", "seedPrice": 30.0, "season": "Late winter to early spring (December to February)", "category": "Vegetable Plant"},
    {"name": "Cauliflower", "seedPrice": 70.0, "season": "Late summer to early autumn (July to September)", "category": "Vegetable Plant"},
    {"name": "Cabbage", "seedPrice": 70.0, "season": "Late summer to early autumn (July to September)", "category": "Vegetable Plant"},
    {"name": "Carrot", "seedPrice": 40.0, "season": "Late summer to early autumn (July to September)", "category": "Vegetable Plant"},
    {"name": "Radish", "seedPrice": 30.0, "season": "Late summer to early autumn (July to September)", "category": "Vegetable Plant"},
    {"name": "Spinach", "seedPrice": 25.0, "season": "Late winter to early spring (December to February)", "category": "Vegetable Plant"},
    {"name": "Okra", "seedPrice": 30.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Bitter Gourd", "seedPrice": 25.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Snake Gourd", "seedPrice": 25.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Bean", "seedPrice": 30.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Pumpkin", "seedPrice": 30.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Cucumber", "seedPrice": 30.0, "season": "Late spring to early summer (March to May)", "category": "Vegetable Plant"},
    {"name": "Bell Pepper", "seedPrice": 40.0, "season": "Late winter to early spring (December to February)", "category": "Vegetable Plant"},
    {"name": "Chili Pepper", "seedPrice": 25.0, "season": "Late winter to early spring (December to February)", "category": "Vegetable Plant"},
    {"name": "Lenol", "seedPrice": 40.0, "season": "Late autumn to early winter (October to November)", "category": "Vegetable Plant"},
]


        # weather and gardening logo

        try:
            weather_image = Image.open("weatherLogo.png")
            resized_weather_image = weather_image.resize((240, 220))
            self.weather_logo_image = ImageTk.PhotoImage(resized_weather_image)

            weather_logo_label = Label(self.root, image=self.weather_logo_image)
            weather_logo_label.place(x=80, y=200)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load or resize weatherLogo.png: {e}")

        try:
            garden_image = Image.open("gardenLogo.png")
            resized_garden_image = garden_image.resize((270, 210))
            self.garden_logo_image = ImageTk.PhotoImage(resized_garden_image)

            garden_logo_label = Label(self.root, image=self.garden_logo_image)
            garden_logo_label.place(x=500, y=200)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load or resize gardenLogo.png: {e}")

        #main Buttons:

        Button(self.root, text="Gardening Options", command=self.gardening_options,
                font=("Arial", 14, "bold"), bg="green", fg="white").place(x=530, y=140)

        Button(self.root, text="Weather Features", command=self.weather_app,
                font=("Arial", 14, "bold"), bg="blue", fg="white").place(x=100, y=140)

        Button(self.root, text="Exit", command=self.root.destroy,
                font=("Arial", 14, "bold"), bg="black", fg="white").place(x=670, y=40)

    #gardening options:
    
    def gardening_options(self):
        gardening_window = Toplevel(self.root)
        gardening_window.title("Gardening Options")
        gardening_window.geometry("800x500+300+100")
        gardening_window.config(bg="#ADD8E6")

        try:
            gardening_icon = PhotoImage(file="gardening.png")
            gardening_window.iconphoto(False, gardening_icon)
        except Exception as e:
            messagebox.showwarning("Warning", f"Icon not found: {e}")

        Label(gardening_window, text="Gardening Options", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

        Button(gardening_window, text="Flower Plants", command=lambda: self.display_tree_names("Flower Plant"),
                font=("Arial", 12, "bold"), bg="pink", fg="white", width=20).pack(pady=10)

        Button(gardening_window, text="Fruit Plants", command=lambda: self.display_tree_names("Fruit Plant"),
                font=("Arial", 12, "bold"), bg="black", fg="white", width=20).pack(pady=10)

        Button(gardening_window, text="Vegetable Plants", command=lambda: self.display_tree_names("Vegetable Plant"),
                font=("Arial", 12, "bold"), bg="purple", fg="white", width=20).pack(pady=10)

    def display_tree_names(self, category):
        tree_window = Toplevel(self.root)
        tree_window.title(f"{category} Trees")
        tree_window.geometry("800x500+300+100")
        tree_window.config(bg="#ADD8E6")

        try:
            tree_icon = PhotoImage(file="gardening.png")
            tree_window.iconphoto(False, tree_icon)
        except Exception as e:
            messagebox.showwarning("Warning", f"Icon not found: {e}")

        Label(tree_window, text=f"{category} Trees", font=("Arial", 16, "bold"), bg="maroon", fg="white").pack(pady=10)

        tree_listbox = Listbox(tree_window, width=50, height=12, font=("Arial", 15), bg="teal", fg="black")
        tree_listbox.pack(pady=30)

        for tree in self.trees:
            if tree["category"] == category:
                tree_listbox.insert(END, tree["name"])

        def view_tree_details():
            selected_tree_index = tree_listbox.curselection()
            if not selected_tree_index:
                messagebox.showerror("Error", "No tree selected.")
                return
            selected_tree_name = tree_listbox.get(selected_tree_index)
            self.display_tree_info(selected_tree_name)

        Button(tree_window, text="View Details", command=view_tree_details,
                font=("Arial", 12, "bold"), bg="maroon", fg="white").pack(pady=10)

    def display_tree_info(self, tree_name):
        tree_detail_window = Toplevel(self.root)
        tree_detail_window.title(f"{tree_name} Details")
        tree_detail_window.geometry("800x500+300+100")
        tree_detail_window.config(bg="#ADD8E6")

        try:
            tree_icon = PhotoImage(file="gardening.png")
            tree_detail_window.iconphoto(False, tree_icon)
        except Exception as e:
            messagebox.showwarning("Warning", f"Icon not found: {e}")

        tree = next((tree for tree in self.trees if tree["name"].lower() == tree_name.lower()), None)
        if tree:
            Label(tree_detail_window, text=f"Name: {tree['name']}", font=("Arial", 18, "bold"), bg="turquoise").pack(pady=35)
            Label(tree_detail_window, text=f"Seed Price: {tree['seedPrice']} BDT", font=("Arial", 14, "bold"), bg="teal").pack(pady=5)
            Label(tree_detail_window, text=f"Season: {tree['season']}", font=("Arial", 14, "bold"), bg="teal").pack(pady=5)
            Label(tree_detail_window, text=f"Category: {tree['category']}", font=("Arial", 14, "bold"), bg="teal").pack(pady=5)
        else:
            Label(tree_detail_window, text="Tree not found.", font=("Arial", 14), fg="red").pack(pady=5)


    def weather_app(self):
        if not os.path.exists("weather_details.py"):
            messagebox.showerror("Error", "weather_details.py not found.")
            return

        try:
            subprocess.Popen(['python', 'weather_details.py'])
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open mainProject.py: {e}")

if __name__ == "__main__":
    root = Tk()
    app = TreeApp(root)
    root.mainloop()
