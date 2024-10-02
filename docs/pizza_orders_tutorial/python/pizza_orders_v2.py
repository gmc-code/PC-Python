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

# Define the prices for each pizza size
prices = {
    "Margherita": {"Small": 5, "Medium": 7, "Large": 10},
    "Pepperoni": {"Small": 6, "Medium": 8, "Large": 11},
    "Hawaiian": {"Small": 6, "Medium": 8, "Large": 11},
    "Veggie": {"Small": 5, "Medium": 7, "Large": 10},
    "BBQ Chicken": {"Small": 7, "Medium": 9, "Large": 12}
}

# Function to take user input for orders
def take_orders():
    orders = []
    while True:
        customer = input("Enter customer name (or 'done' to finish): ")
        if customer.lower() == 'done':
            break
        pizza = input("Enter pizza type: ")
        size = input("Enter pizza size (Small, Medium, Large): ")
        quantity = int(input("Enter quantity: "))
        orders.append((customer, pizza, size, quantity))
    return orders

# Take orders from user
orders = take_orders()

# Process the orders
result, total_cost, individual_costs = collect_pizza_orders(orders, prices)
print(result)
print(f"Total cost for the group: ${total_cost}")
print("Cost per person:")
for customer, cost in individual_costs.items():
    print(f"{customer}: ${cost}")

# Example Output:
# Enter customer name (or 'done' to finish): Alice
# Enter pizza type: Margherita
# Enter pizza size (Small, Medium, Large): Large
# Enter quantity: 2
# Enter customer name (or 'done' to finish): done
# {
#     'Margherita': {'Alice': {'Large': 2}, 'total_cost': 20}
# }
# Total cost for the group: $20
# Cost per person:
# Alice: $20
