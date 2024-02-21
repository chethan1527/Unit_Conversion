import tkinter as tk
from tkinter import ttk

def cm_to_feet(cm):
    try:
        cm = float(cm)
        feet = cm / 30.48
        return f"{feet:.2f} feet"
    except ValueError:
        return "Invalid input"

def feet_to_inches(feet):
    try:
        feet = float(feet)
        inches = feet * 12
        return f"{inches:.2f} inches"
    except ValueError:
        return "Invalid input"

def sqft_to_sqm(sqft):
    try:
        sqft = float(sqft)
        sqm = sqft / 10.764
        return f"{sqm:.2f} square meters"
    except ValueError:
        return "Invalid input"

def sqft_to_hectare_acres(sqft):
    try:
        sqft = float(sqft)
        hectares = sqft / 107639.104
        acres = sqft / 43560
        return f"{hectares:.2f} hectares\n{acres:.2f} acres"
    except ValueError:
        return "Invalid input"

def clear_all():
    conversion_options.set("Select")
    entry_value.delete(0, tk.END)
    result_label.config(text="")


def display_result():
    selected_option = conversion_options.get()
    value = entry_value.get()
    if selected_option == "Select":
        result_label.config(text="Please select a conversion option", fg="red", font=("Helvetica", 16))
    elif selected_option == "Centimeter to Feet":
        result_label.config(text=cm_to_feet(value), fg="green", font=("Helvetica", 16))
    elif selected_option == "Feet to Inches":
        result_label.config(text=feet_to_inches(value), fg="green", font=("Helvetica", 16))
    elif selected_option == "Sqft to Sqm":
        result_label.config(text=sqft_to_sqm(value), fg="green", font=("Helvetica", 16))
    elif selected_option == "Sqft to Hectare/Acres":
        result_label.config(text=sqft_to_hectare_acres(value), fg="green", font=("Helvetica", 16))



# Create main window
root = tk.Tk()
root.title("Unit Converter")

# Load background image
bg_image = tk.PhotoImage(file="tape.png")

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relx=0.5, rely=0.5, anchor='center')

# Heading
heading_label = tk.Label(root, text="Unit Converter", font=("Helvetica", 20, "bold"))
heading_label.pack(pady=10)
conversion_label = tk.Label(root, text="Conversion Type:", font=("Helvetica", 12))
conversion_label.pack()
# Dropdown box for conversion options
conversion_options = ttk.Combobox(root,values=[
    "Centimeter to Feet",
    "Feet to Inches",
    "Sqft to Sqm",
    "Sqft to Hectare/Acres"
])
conversion_options.set("Select")  # Set default value
conversion_options.pack()
# Labels and entry widgets
tk.Label(root, text="Value:", anchor='center').pack()
entry_value = tk.Entry(root)
entry_value.pack()
convert_button = tk.Button(root, text="Convert", command=display_result)
convert_button.pack(pady=5)
result_label = tk.Label(root, text="", anchor='center')
result_label.pack(pady=10)

# Clear all button
clear_button = tk.Button(root, text="Clear All", command=clear_all)
clear_button.pack(pady=5)

root.mainloop()





