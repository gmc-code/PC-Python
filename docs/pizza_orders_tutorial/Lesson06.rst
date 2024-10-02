================================================
Pizza orders Lesson 6: Displaying Costs
================================================

Lesson 6: Displaying Costs
--------------------------
- **Objective**: Display the cost per pizza and total cost.
- **Content**:
  - Using StringVar to display costs.
  - Updating costs dynamically based on selections.

Lesson 6: Displaying Costs
==========================

Objective
---------
Display the cost per pizza and total cost.

Content
-------

1. Using StringVar to Display Costs

.. code-block:: python

   cost_display_var = tk.StringVar(root)
   cost_display_var.set("Cost per pizza: $0")
   tk.Label(root, textvariable=cost_display_var).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

   total_cost_var = tk.StringVar(root)
   total_cost_var.set("Total cost: $0")
   tk.Label(root, textvariable=total_cost_var).grid(row=5, column=0, columnspan=2, padx=10, pady=5)

   - ``cost_display_var = tk.StringVar(root)``: Creates a StringVar to hold the cost per pizza.
   - ``cost_display_var.set("Cost per pizza: $0")``: Sets the initial value of the cost display.
   - ``tk.Label(root, textvariable=cost_display_var)``: Creates a label that displays the cost per pizza.
   - ``total_cost_var = tk.StringVar(root)``: Creates a StringVar to hold the total cost.
   - ``total_cost_var.set("Total cost: $0")``: Sets the initial value of the total cost display.
   - ``tk.Label(root, textvariable=total_cost_var)``: Creates a label that displays the total cost.

2. Updating Costs Dynamically Based on Selections
   - Use the ``trace`` method of ``StringVar`` to update the costs whenever the pizza type, size, or quantity changes.

.. code-block:: python

   pizza_var.trace("w", update_cost_display)
   size_var.trace("w", update_cost_display)
   quantity_var.trace("w", update_total_cost)

3. Additional Examples
   - Displaying the cost of drinks:

.. code-block:: python

   drink_cost_var = tk.StringVar(root)
   drink_cost_var.set("Cost per drink: $0")
   tk.Label(root, textvariable=drink_cost_var).grid(row=6, column=0, columnspan=2, padx=10, pady=5)
