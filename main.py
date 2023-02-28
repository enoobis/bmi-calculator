import tkinter as tk

# Define the root window
root = tk.Tk()
root.title("BMI Calculator")
root.config(bg="#24292e")

# Define the function to calculate BMI
def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height / 100) ** 2
    bmi_label.config(text=f"BMI: {bmi:.2f}")
    
    # Set the color of the result label based on BMI value
    if bmi < 18.5:
        bmi_label.config(fg="#f1e05a")
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_label.config(fg="#97ca00")
    elif bmi >= 25 and bmi <= 29.9:
        bmi_label.config(fg="#f1e05a")
    else:
        bmi_label.config(fg="#d73a49")

# Create the widgets
height_label = tk.Label(root, text="Height (cm):", bg="#24292e", fg="#c8c8c8")
height_entry = tk.Entry(root)
weight_label = tk.Label(root, text="Weight (kg):", bg="#24292e", fg="#c8c8c8")
weight_entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi, bg="#28a745", fg="#fff")
bmi_label = tk.Label(root, text="", bg="#24292e", fg="#fff", font=("Arial", 16, "bold"))

# Add the widgets to the grid
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry.grid(row=0, column=1, padx=10, pady=10)
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry.grid(row=1, column=1, padx=10, pady=10)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
bmi_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
