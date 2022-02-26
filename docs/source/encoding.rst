.. _encoding:

Encoding
========

Encoding into oceanscript looks challenging at first,
but it sure doesn't take too long to get into the swing of it.

Start by visualizing 4 boxes. These boxes can be used to write
oceanscript, and in my opinion it is the best way to get started.

^^^^^^^^^^^^^^^^^
Box Configuration
^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: /tables/all.csv
   :widths: 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
   :align: center

When writing a character in oceanscript, you should look from left to
right at the row and column indicators on each box.

We need to check three things:

1. What row is my character in?
2. What column is my character in?
3. What box is my character in?

.. tip::

   - When checking for the row, look at the most-left column of the table.
   - When checking for the column, look at the top or bottom row of the entire table.
   - When checking for the box, look at the most-right column of the table.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Single Letter Obtainment BOX-1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lets try and write the letter "d". "d" is in box 1.

.. csv-table::
   :file: /tables/t1.csv
   :widths: 2 2 2 2 2
   :align: left

**Row**

   As we look across to our table above, the letter "d" is on
   the middle row. Looking to the **left**, that means we start with
   ``~``.

**Column**

   Looking directly above where "d" is in the table, our next
   character should be ``<``.

**Box**

   We are in box **1**, so we add 1 dot on the end (``.``). The table also tells
   us to, on the most-right column.

Joining all these components together, we get ``~<.`` - and that is how you write
the letter "d" in oceanscript!

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Letter Obtainment in other boxes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now lets have a look at writing a character from a different box.
Lets pick "s" for example, a character used quite a lot. "s" is in box 3:

.. csv-table::
   :file: /tables/t3.csv
   :widths: 2 2 2 2 2
   :align: left

**Row**

   Looking to the **left**, we start with ``^``.

**Column**

   Looking directly above where "s" is in the table, our next
   character should be ``<``.

**Box**

   We are in box **3**, so we add 3 dots on the end (``...``). The table also tells
   us to, on the most-right column.

Joining all these components together, we get ``^<...`` - and that is how you write
the letter "s" in oceanscript.

Unfortunately, characters in BOX-4 work slightly differently. In BOX-4 are the numbers 1-9:

.. csv-table::
   :file: /tables/t4.csv
   :widths: 2 2 2 2 2
   :align: left

Instead of adding **4** dots (as you'd expect), you instead just add the letter "o".
So the number 7 in oceanscript would be ``_<o`` instead of ``_<....``.

^^^^^^^^^^^^^
Forming Waves
^^^^^^^^^^^^^

When we've encoded a character into oceanscript, it is referred to as a wave. For example,
``^<..`` is a **wave** representing the letter "J". The above examples demonstrate how waves
can be formed.

^^^^^^^^^^^^^
Forming Tides
^^^^^^^^^^^^^

Tides are the joinings of waves in oceanscript - to form a word. To form a word,
simply join the waves together. Here is each letter encoded as a wave in the word "hello":

- h = ``_-.``
- e = ``~-.``
- l = ``^>..``
- l = ``^>..``
- o = ``~>..``

To form the word hello, we will join these waves together. "hello" in oceanscript will look like
this: ``_-.~-.^>..^>..~>..``.

^^^^^^^^^^^^^^
Forming Oceans
^^^^^^^^^^^^^^

This is the final escalation of encoding. "Ocean" is the name given to a collection of tides to
form sentences, paragraphs, even essays if you wish. A space in oceanscript is represented
as ``,``, which is put in between each wave you want to join together. Here, we have two waves
representing the words "hello" and "world":

``hello`` -> ``_-.~-.^>..^>..~>..``

``world`` -> ``~-...~>.._>..^>..~<.``

To join these waves together, we just need to put our comma (``,``) in between them. "hello world"
would look like this: ``_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.``. This is an ocean.

Capitalization
==============

The tables that have been shown above only contain lower-case letters and numbers.
To write a capital letter, we use the *splash indicator* which looks like this: ``*``.
This indicator prefixes each wave which requires capitalization.

Here we have the letter "h": ``_-.``. To capitalize, we add our splash at the start of the wave,
so it will look like this: ``*_-.``. If you wanted to write a whole tide in capitals, you'd need
to use the splash indicator for each wave in that tide.

Non a-Z/0-9 Characters
======================

You can now write "Hello world", or "How are you" - but what about punctuation!

In oceanscript, if a character does not appear in the tables, it doesn't belong in the ocean.
We need to use a **raft** in order to write said character. A raft is denoted by the character ``=``,
and it works just like the splash indicator, we prefix the given character with it. Rafts are **NOT**
allowed for a-Z and 0-9, but are **required** for any other character.

.. admonition:: Example

   Is ``?`` in a-Z/0-9? No. We need to use a raft for this character.
   It would look like this ``=?``.

Rafts can only take one passenger at a time, so to write an ellipsis (...), we would need
3 rafts (``=.=.=.``).

Now we can write "How are you?" -> ``*_-.~>..~-...,^<._>.~-.,_<...~>..^>...=?``

Literal Line Breaks
===================

Be careful when writing line breaks in oceanscript, seeing as a line break would represent a space
and not a **literal** line break. To do so literally, use the ``%`` character.

.. admonition:: Example

   ```
   H
   I
   ```

   This word is both fully capitalized and uses a line break to split the
   two letters (for whatever reason). It would be written as ``*_-.%*_>.``

   ```
   I - I
   K - Know
   R - Right
   ```

   This acronym uses line breaks, and would be encoded to look like this:

   .. code-block::

      *_>.,=-,*_>.%*^-..,=-,*^-..~-..~>..~-...%*_>..,=-,*_>.._>._<._-.^-...
