import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pizza Order System")
root.geometry("400x300")

# Add labels and entry widgets for customer name input.
tk.Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
customer_entry = tk.Entry(root)
customer_entry.grid(row=0, column=1, padx=10, pady=5)

# additional
tk.Label(root, text="Address:").grid(row=1, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1, padx=10, pady=5)

# Add radio buttons for selecting pizza types
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_frame = tk.Frame(root)
pizza_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")

for pizza in ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]:
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza).pack(anchor="w")

# Add radio buttons for drink options:
drink_var = tk.StringVar(root)
drink_var.set("Coke")
drink_frame = tk.Frame(root)
drink_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

for drink in ["Coke", "Pepsi", "Water"]:
    tk.Radiobutton(drink_frame, text=drink, variable=drink_var, value=drink).pack(anchor="w")

# Run the application
root.mainloop()
