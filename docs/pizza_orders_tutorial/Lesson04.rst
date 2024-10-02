==============================================================
Pizza orders Lesson 4: Adding Radio Buttons for Pizza Sizes
==============================================================

Lesson 4: Adding Radio Buttons for Pizza Sizes
----------------------------------------------
- **Objective**: Add radio buttons for selecting pizza sizes.
- **Content**:
  - Creating and positioning radio buttons for sizes.
  - Updating the cost display based on selection.

Lesson 4: Adding Radio Buttons for Pizza Sizes
==============================================

Objective
---------
Add radio buttons for selecting pizza sizes.

Content
-------

1. Creating and Positioning Radio Buttons for Sizes

.. code-block:: python

   size_var = tk.StringVar(root)
   size_var.set("Small")
   size_frame = tk.Frame(root)
   size_frame.grid(row=2, column=1, padx=10, pady=5, sticky="w")

   for size in ["Small", "Medium", "Large"]:
       tk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w")

   - ``size_var = tk.StringVar(root)``: Creates a StringVar to hold the value of the selected size.
   - ``size_var.set("Small")``: Sets the default value of the size radio button group.
   - ``size_frame = tk.Frame(root)``: Creates a frame to contain the size radio buttons.
   - ``.grid(row=2, column=1, padx=10, pady=5, sticky="w")``: Positions the frame in the grid layout.
   - ``tk.Radiobutton(size_frame, text=size, variable=size_var, value=size)``: Creates a radio button for each size, associating it with the StringVar.

2. Updating the Cost Display Based on Selection
   - You can use the ``trace`` method of ``StringVar`` to call a function whenever the value changes.

.. code-block:: python

   def update_cost_display(*args):
       pizza = pizza_var.get()
       size = size_var.get()
       if pizza and size:
           cost = prices[pizza][size]
           cost_display_var.set(f"Cost per pizza: ${cost}")

   size_var.trace("w", update_cost_display)

3. Additional Examples
   - Creating radio buttons for crust types:

.. code-block:: python

   crust_var = tk.StringVar(root)
   crust_var.set("Thin")
   crust_frame = tk.Frame(root)
   crust_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")

   for crust in ["Thin", "Thick", "Stuffed"]:
       tk.Radiobutton(crust_frame, text=crust, variable=crust_var, value=crust).pack(anchor="w")
