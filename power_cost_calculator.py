import tkinter as tk
from tkinter import messagebox
import sys

def calculate_cost():
    try:
        watt = int(entry_watt.get())
        usage_time = int(entry_usage_time.get())
        electricity_rate = float(entry_electricity_rate.get().replace(",", "."))
        
        # Electricity cost calculation
        cost = watt * usage_time * electricity_rate / 1000
        messagebox.showinfo("Result", f"The cost of using your computer is: {cost:.2f} USD") #TL için {cost} TL
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Power Cost Calculator")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Create and place labels and entries
label_watt = tk.Label(root, text="Power Consumption (Watt):", bg="#f2f2f2", font=("Arial", 12))
label_watt.pack(pady=10)
entry_watt = tk.Entry(root)
entry_watt.pack(pady=5)

label_usage_time = tk.Label(root, text="Usage Time (Hours):", bg="#f2f2f2", font=("Arial", 12))
label_usage_time.pack(pady=10)
entry_usage_time = tk.Entry(root)
entry_usage_time.pack(pady=5)

label_electricity_rate = tk.Label(root, text="Electricity Rate (USD/kWh):", bg="#f2f2f2", font=("Arial", 12))
label_electricity_rate.pack(pady=10)
entry_electricity_rate = tk.Entry(root)
entry_electricity_rate.pack(pady=5)

# Create and place the calculate button
button_calculate = tk.Button(root, text="Calculate Cost", command=calculate_cost, bg="#4CAF50", fg="white", font=("Arial", 12))
button_calculate.pack(pady=20)

# Run the application
try:
    root.mainloop()
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
