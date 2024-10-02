================================================
Pizza orders Lesson 1: Adding Orders
================================================

Lesson 7: Adding Orders
-----------------------
- **Objective**: Add functionality to add orders.
- **Content**:
  - Creating an add order button.
  - Writing the `add_order` function.
  - Validating input and updating the order list.

Lesson 7: Adding Orders
=======================

Objective
---------
Add functionality to add orders.

Content
-------

1. Creating an Add Order Button

.. code-block:: python

   add_button = tk.Button(root, text="Add Order", command=add_order, bg=button_bg, fg=button_fg)
   add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

   - ``tk.Button(root, text="Add Order", command=add_order, bg=button_bg, fg=button_fg)``: Creates a button with the text "Add Order" and assigns the ``add_order`` function to be called when the button is clicked.
   - ``.grid(row=6, column=0, columnspan=2, padx=10, pady=10)``: Positions the button in the grid layout.

2. Writing the ``add_order`` Function

.. code-block:: python

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

   - ``add_order``: Function to add an order to the list.
   - ``customer = customer_entry.get()``: Retrieves the customer name from the entry widget.
   - ``pizza = pizza_var.get()``: Retrieves the selected pizza type.
   - ``size = size_var.get()``: Retrieves the selected pizza size.
   - ``quantity = int(quantity_var.get())``: Retrieves the selected quantity and converts it to an integer.
   - ``messagebox.showerror("Input Error", "Please enter the customer name.")``: Displays an error message if the customer name is not entered.
   - ``orders.append((customer, pizza, size, quantity))``: Adds the order to the list of orders.
   - ``update_order_list()``: Updates the order list display.
   - ``update_customer_menu()``: Updates the customer menu for deleting orders.
   - ``customer_entry.delete(0, tk.END)``: Clears the customer name entry widget.
   - ``quantity_var.set("1")``: Resets the quantity to 1.
   -