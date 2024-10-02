import tkinter as tk
from tkinter import messagebox

# Define the prices for each pizza size
prices = {
    "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
    "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
    "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
    "Veggie": {"Small": 5, "Medium": 7, "Large": 10},
    "BBQ Chicken": {"Small": 7, "Medium": 9, "Large": 12}
}

orders = []

def update_cost_display(*args):
    pizza = pizza_var.get()
    size = size_var.get()
    if pizza and size:
        cost = prices[pizza][size]
        cost_display_var.set(f"Cost per pizza: ${cost}")
        update_total_cost()

def update_total_cost(*args):
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = int(quantity_var.get())
    if pizza and size:
        total_cost = prices[pizza][size] * quantity
        total_cost_var.set(f"Total cost: ${total_cost}")

def add_order():
    customer = customer_entry.get()
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = int(quantity_var.get())

    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="red")
        return
    else:
        customer_entry.config(bg="white")

    orders.append((customer, pizza, size, quantity))
    update_order_list()
    update_customer_menu()
    customer_entry.delete(0, tk.END)
    quantity_var.set("1")
    total_cost_var.set("Total cost: $0")

def delete_order():
    customer = delete_customer_var.get()
    if not customer:
        messagebox.showerror("Input Error", "Please select a customer to delete.")
        return

    global orders
    orders = [order for order in orders if order[0] != customer]
    update_order_list()
    update_customer_menu()

def update_order_list():
    order_list.delete(1.0, tk.END)
    result, total_cost, individual_costs = collect_pizza_orders(orders, prices)
    for order in orders:
        customer, pizza, size, quantity = order
        order_list.insert(tk.END, f"{customer} ordered {quantity} {size} {pizza}(s)\n")
    order_list.insert(tk.END, f"\nTotal cost for the group: ${total_cost}\n")
    order_list.insert(tk.END, "Cost per person:\n")
    for customer, cost in individual_costs.items():
        order_list.insert(tk.END, f"{customer}: ${cost}\n")

def update_customer_menu():
    customers = list(set(order[0] for order in orders))
    delete_customer_menu['menu'].delete(0, 'end')
    for customer in customers:
        delete_customer_menu['menu'].add_command(label=customer, command=tk._setit(delete_customer_var, customer))

def collect_pizza_orders(orders, prices, result=None):
    if result is None:
        result = dict()
    total_cost = 0
    individual_costs = {}

    for order in orders:
        customer, pizza, size, quantity = order
        if pizza not in result:
            result[pizza] = {}
        if customer in result[pizza]:
            if size in result[pizza][customer]:
                result[pizza][customer][size] += quantity
            else:
                result[pizza][customer][size] = quantity
        else:
            result[pizza][customer] = {size: quantity}

        # Calculate cost for each pizza
        cost = prices[pizza][size] * quantity
        total_cost += cost

        # Add cost to individual customer
        if customer in individual_costs:
            individual_costs[customer] += cost
        else:
            individual_costs[customer] = cost

        if 'total_cost' in result[pizza]:
            result[pizza]['total_cost'] += cost
        else:
            result[pizza]['total_cost'] = cost

    return result, total_cost, individual_costs

# Create the main window
root = tk.Tk()
root.title("Pizza Order System")
root.configure(bg="#f0f0f0")

# Style configurations
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 14)
entry_bg = "#ffffff"
button_bg = "#4CAF50"
button_fg = "#ffffff"
highlight_bg = "#ffcccc"
delete_button_bg = "#ff6666"

# Customer name
tk.Label(root, text="Customer Name:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
customer_entry = tk.Entry(root, bg=entry_bg, font=entry_font, width=30)
customer_entry.grid(row=0, column=1, padx=10, pady=5)

# Pizza type
tk.Label(root, text="Pizza Type:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_var.trace("w", update_cost_display)
pizza_frame = tk.Frame(root, bg="#f0f0f0")
pizza_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
for pizza in prices.keys():
    tk.Radiobutton(pizza_frame, text=pizza, variable=pizza_var, value=pizza, bg="#f0f0f0").pack(anchor="w")

# Pizza size
tk.Label(root, text="Pizza Size:", font=label_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
size_var = tk.StringVar(root)
size_var.set("Small")
size_var.trace("w", update_cost_display)
size_frame = tk.Frame(root, bg="#f0f0f0")
size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")
for size in ["Small", "Medium", "Large"]:
    tk.Radiobutton(size_frame, text=size, variable=size_var, value=size, bg="#f0f0f0").pack(anchor="w")

# Quantity
tk.Label(root, text="Quantity:", font=label_font, bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
quantity_var = tk.StringVar(root)
quantity_var.set("1")
quantity_menu = tk.OptionMenu(root, quantity_var, *[str(i) for i in range(1, 31)])
quantity_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")
quantity_var.trace("w", update_total_cost)

# Cost display
cost_display_var = tk.StringVar(root)
cost_display_var.set("Cost per pizza: $0")
tk.Label(root, textvariable=cost_display_var, font=label_font, bg="#f0f0f0").grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Total cost display
total_cost_var = tk.StringVar(root)
total_cost_var.set("Total cost: $0")
tk.Label(root, textvariable=total_cost_var, font=label_font, bg="#f0f0f0").grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Add order button
add_button = tk.Button(root, text="Add Order", command=add_order, bg=button_bg, fg=button_fg)
add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Order list
order_list = tk.Text(root, height=10, width=50, bg=entry_bg)
order_list.grid(row=0, column=2, rowspan=8, padx=10, pady=10)

# Delete order section
tk.Label(root, text="Delete Order for Customer:", font=label_font, bg="#f0f0f0").grid(row=8, column=0, padx=10, pady=5, sticky="e")
delete_customer_var = tk.StringVar(root)
delete_customer_menu = tk.OptionMenu(root, delete_customer_var, "")
delete_customer_menu.grid(row=8, column=1, padx=10, pady=5, sticky="w")
delete_button = tk.Button(root, text="Delete Order", command=delete_order, bg=delete_button_bg, fg=button_fg)
delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
