================================================
Pizza orders Lesson 8: Deleting Orders
================================================

- **Objective**: Add functionality to delete orders.
- **Content**:

  - Creating a delete order section.
  - Writing the `delete_order` function.
  - Updating the customer menu dynamically.


Creating a Delete Order Section
------------------------------------

.. code-block:: python

    tk.Label(root, text="Delete Order for Customer:", font=label_font, bg="#f0f0f0").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    delete_customer_var = tk.StringVar(root)
    delete_customer_menu = tk.OptionMenu(root, delete_customer_var, "")
    delete_customer_menu.grid(row=8, column=1, padx=10, pady=5, sticky="w")
    delete_button = tk.Button(root, text="Delete Order", command=delete_order, bg=delete_button_bg, fg=button_fg)
    delete_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

- ``tk.Label(root, text="Delete Order for Customer:", font=label_font, bg="#f0f0f0")``: Creates a label for the delete order section.
- ``delete_customer_var = tk.StringVar(root)``: Creates a StringVar to hold the selected customer for deletion.
- ``delete_customer_menu = tk.OptionMenu(root, delete_customer_var, "")``: Creates an OptionMenu for selecting the customer to delete.
- ``delete_button = tk.Button(root, text="Delete Order", command=delete_order, bg=delete_button_bg, fg=button_fg)``: Creates a button to delete the selected order.

1. Writing the ``delete_order`` Function

.. code-block:: python

   def delete_order():
       customer = delete_customer_var.get()
       if not customer:
           messagebox.showerror("Input Error", "Please select a customer to delete.")
           return

       global orders
       orders = [order for order in orders if order != customer]
       update_order_list()
       update_customer_menu()

   - ``delete_order``: Function to delete an order from the list.
   - ``customer = delete_customer_var.get()``: Retrieves the selected customer from the OptionMenu.
   - ``orders = [order for order in orders if order != customer]``: Removes the selected customer's orders from the list.
   - ``update_order_list()``: Updates the order list display.
   - ``update_customer_menu()``: Updates the customer menu for deleting orders.

3. Updating the Customer Menu Dynamically

.. code-block:: python

   def update_customer_menu():
       customers = list(set(order for order in orders))
       delete_customer_menu['menu'].delete(0, 'end')
       for customer in customers:
           delete_customer_menu['menu'].add_command(label=customer, command=tk._setit(delete_customer_var, customer))

   - ``update_customer_menu``: Function to update the customer menu.
   - ``customers = list(set(order for order in orders))``: Creates a list of unique customers from the orders.
   - ``delete_customer_menu['menu'].delete(0, 'end')``: Clears the current menu options.
   - ``delete_customer_menu['menu'].add_command(label=customer, command=tk._setit(delete_customer_var, customer))``: Adds each customer to the menu.
