.. _encoding:

Encoding
========

Encoding into oceanscript looks challenging at first,
but it sure doesn't take too long to get into the swing of it.

Start by visualizing 4 boxes. These boxes can be used to write
oceanscript, and in my opinion it is the best way to get started.
They look like this:

.. csv-table::
   :file: /tables/all.csv
   :widths: 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
   :align: center

When writing a character in oceanscript, you should look from left to
right at the row and column indicators on each box.

Lets zoom in on the first BOX-1.

.. csv-table::
   :file: /tables/t1.csv
   :widths: 2 2 2 2 2
   :align: center

We need to check three things:

1. What row is my character in?
2. What column is my character in?
3. What box is my character in?

.. admonition:: Example

   Lets try and write the letter "d".

   **Row**

      As we look across to our table above, the letter "d" is on
      the middle row. Looking to the left, that means we start with
      ``~``.

   **Column**

      Looking directly above where "d" is in the table, our next
      character should be ``<``.

   **Box**

      We are in box **1**, so we add 1 dot on the end (``.``). The table also tells
      us to, on the most-right column.

   Joining all these components together, we get ``~<.`` - and that is how you write
   the letter "d" in oceanscript!
