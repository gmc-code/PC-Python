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


# Run the application
root.mainloop()
