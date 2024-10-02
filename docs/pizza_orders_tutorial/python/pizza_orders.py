def collect_pizza_orders(orders, prices, result=None):
    if result is None:
        result = dict()
    total_cost = 0
    individual_costs = {}

    for order in orders:
        customer, pizza, size = order
        if pizza not in result:
            result[pizza] = {}
        if customer in result[pizza]:
            result[pizza][customer].append(size)
        else:
            result[pizza][customer] = [size]

        # Calculate cost for each pizza
        cost = prices[pizza][size]
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

orders = [
    ("Alice", "Margherita", "Large"),
    ("Bob", "Pepperoni", "Medium"),
    ("Alice", "Hawaiian", "Small"),
    ("Charlie", "Veggie", "Large"),
    ("Bob", "BBQ Chicken", "Large"),
    ("Alice", "Margherita", "Medium")
]

result, total_cost, individual_costs = collect_pizza_orders(orders, prices)
print(result)
print(f"Total cost for the group: ${total_cost}")
print("Cost per person:")
for customer, cost in individual_costs.items():
    print(f"{customer}: ${cost}")

# Output:
# {
#     'Margherita': {'Alice': ['Large', 'Medium'], 'total_cost': 17},
#     'Pepperoni': {'Bob': ['Medium'], 'total_cost': 8},
#     'Hawaiian': {'Alice': ['Small'], 'total_cost': 6},
#     'Veggie': {'Charlie': ['Large'], 'total_cost': 10},
#     'BBQ Chicken': {'Bob': ['Large'], 'total_cost': 12}
# }
# Total cost for the group: $53
# Cost per person:
# Alice: $23
# Bob: $20
# Charlie: $10
