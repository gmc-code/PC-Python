==================================================
Pizza orders Lesson 10: Final Touches and Styling
==================================================

Lesson 10: Final Touches and Styling
------------------------------------
- **Objective**: Add final touches and improve the GUI styling.
- **Content**:
  - Adding styles to widgets.
  - Improving the layout and appearance.
  - Final review and testing.

Lesson 10: Final Touches and Styling
====================================

Objective
---------
Add final touches and improve the GUI styling.

Content
-------

1. Adding Styles to Widgets

.. code-block:: python

   label_font = ("Helvetica", 12)
   entry_font = ("Helvetica", 14)
   entry_bg = "#ffffff"
   button_bg = "#4CAF50"
   button_fg = "#ffffff"
   highlight_bg = "#ffcccc"
   delete_button_bg = "#ff6666"

   - ``label_font = ("Helvetica", 12)``: Sets the font for labels.
   - ``entry_font = ("Helvetica", 14)``: Sets the font for entry widgets.
   - ``entry_bg = "#ffffff"``: Sets the background color for entry widgets.
   - ``button_bg = "#4CAF50"``: Sets the background color for buttons.
   - ``button_fg = "#ffffff"``: Sets the foreground color for buttons.
   - ``highlight_bg = "#ffcccc"``: Sets the background color for highlighting errors.
   - ``delete_button_bg = "#ff6666"``: Sets the background color for the delete button.

2. Improving the Layout and Appearance
   - Adjust the padding, alignment, and size of widgets to create a more polished look.

.. code-block:: python

   tk.Label(root, text="Customer Name:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
   customer_entry = tk.Entry(root, bg=entry_bg, font=entry_font, width=30)
   customer_entry.grid(row=0, column=1, padx=10, pady=5)

   - ``sticky="e"``: Aligns the label to the right (east).
   - ``width=30``: Sets the width of the entry widget.

3. Final Review and Testing
   - Test the application to ensure all features work as expected.
   - Make any necessary adjustments to improve functionality and user experience.
