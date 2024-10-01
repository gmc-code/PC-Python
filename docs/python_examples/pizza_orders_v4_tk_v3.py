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

def add_order():
    customer = customer_entry.get()
    pizza = pizza_var.get()
    size = size_var.get()
    quantity = quantity_entry.get()

    if not customer:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        customer_entry.config(bg="red")
        return
    else:
        customer_entry.config(bg="white")

    if not quantity.isdigit() or int(quantity) <= 0:
        quantity = 1
    else:
        quantity = int(quantity)

    orders.append((customer, pizza, size, quantity))
    update_order_list()
    update_customer_menu()
    customer_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

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

# Customer name
tk.Label(root, text="Customer Name:").grid(row=0, column=0)
customer_entry = tk.Entry(root)
customer_entry.grid(row=0, column=1)

# Pizza type
tk.Label(root, text="Pizza Type:").grid(row=1, column=0)
pizza_var = tk.StringVar(root)
pizza_var.set("Margherita")
pizza_menu = tk.OptionMenu(root, pizza_var, *prices.keys())
pizza_menu.grid(row=1, column=1)

# Pizza size
tk.Label(root, text="Pizza Size:").grid(row=2, column=0)
size_var = tk.StringVar(root)
size_var.set("Small")
size_menu = tk.OptionMenu(root, size_var, "Small", "Medium", "Large")
size_menu.grid(row=2, column=1)

# Quantity
tk.Label(root, text="Quantity:").grid(row=3, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=3, column=1)

# Add order button
add_button = tk.Button(root, text="Add Order", command=add_order)
add_button.grid(row=4, column=0, columnspan=2)

# Order list
order_list = tk.Text(root, height=10, width=50)
order_list.grid(row=5, column=0, columnspan=2)

# Delete order section
tk.Label(root, text="Delete Order for Customer:").grid(row=6, column=0)
delete_customer_var = tk.StringVar(root)
delete_customer_menu = tk.OptionMenu(root, delete_customer_var, "")
delete_customer_menu.grid(row=6, column=1)
delete_button = tk.Button(root, text="Delete Order", command=delete_order)
delete_button.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()
