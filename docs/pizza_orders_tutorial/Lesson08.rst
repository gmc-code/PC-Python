================================================
Pizza orders Lesson 8: Displaying Orders
================================================

Lesson 8: Displaying Orders
---------------------------
- **Objective**: Display the list of orders.
- **Content**:
  - Using a Text widget to display orders.
  - Formatting the order display.
  - Updating the order list dynamically.

Lesson 8: Displaying Orders
===========================

Objective
---------
Display the list of orders.

Content
-------

1. Using a Text Widget to Display Orders

.. code-block:: python

   order_list = tk.Text(root, height=10, width=50, bg=entry_bg)
   order_list.grid(row=0, column=2, rowspan=8, padx=10, pady=10)

   - ``order_list = tk.Text(root, height=10, width=50, bg=entry_bg)``: Creates a Text widget to display the list of orders.
   - ``.grid(row=0, column=2, rowspan=8, padx=10, pady=10)``: Positions the Text widget in the grid layout.

2. Formatting the Order Display

.. code-block:: python

   def update_order_list():
       order_list.delete(1.0, tk.END)
       for order in orders:
           customer, pizza, size, quantity = order
           order_list.insert(tk.END, f"{customer} ordered {quantity} {size} {pizza}(s)\n")

   - ``order_list.delete(1.0, tk.END)``: Clears the Text widget.
   - ``order_list.insert(tk.END, f"{customer} ordered {quantity} {size} {pizza}(s)\n")``: Inserts the formatted order details into the Text widget.

3. Updating the Order List Dynamically
   - Call ``update_order_list()`` whenever an order is added or deleted.

.. code-block:: python

   orders.append((customer, pizza, size, quantity))
   update_order_list()
