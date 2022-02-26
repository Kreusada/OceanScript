.. _decoding:

Decoding
========

.. caution::

    Please read the :doc:`encoding guide <encoding>` before
    reading here, as the documentation has been written in this
    order.

By the end of this documentation, you should be able to decode
oceanscript into "normal" text. When decoding, it's best to split
the tides/oceans back into waves, so you can then work on decoding
each wave instead of having a cluster of weird characters in your face.

^^^^^^^^^^^^^^^
Splitting Waves
^^^^^^^^^^^^^^^

.. note::

    The :func:`~oceanscript.splitwaves` function can split into waves
    for you in Python.

We'll use ``*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!`` ("Hello world!")
in a demo here. Lets start by splitting the ocean into tides. We'll find
every instance of ``,`` and split the ocean there.

- ``*_-.~-.^>..^>..~>..``
- ``~-...~>.._>..^>..~<.=!``

We now have two tides (one saying "Hello", the other saying "World!"). A
vitally important thing to remember when decoding oceanscript is that **every**
wave will end in ``.``, unless it is a number from 1-9, then it will end with ``o``.
Characters on rafts can easily be identified too.

In the first tide (``*_-.~-.^>..^>..~>..``), after each discontinuation of a sequence
of dots, we will split the tide there.

- ``*_-.``
- ``~-.``
- ``^>..``
- ``^>..``
- ``~>..``

Notice how each wave ends with ``.`` and does **not** start with ``.``? Now we need to split
the second tide. Don't be thrown off by the fact that there is a raft - they are very easy to
split from the tide.

- ``~-...``
- ``~>..``
- ``_>..``
- ``^>..``
- ``~<.``
- ``=!``

Now we've split our tides into waves, we can decode each one. Simply refer to the encoding guide,
but do it in reverse.

^^^^^^^^^^^^^^^^
Unboarding Rafts
^^^^^^^^^^^^^^^^

Rafts are so easy to decode, simply remove the raft!

.. admonition:: Example

    - ``=[`` -> ``[``
    - ``==`` -> ``=``

    .. warning::
        
        Double rafting (``==``) may become illegal in the future seeing
        as, realistically, it doesn't make any sense. Why raft a raft?

        The likelihood is that a literal ``=`` character will obtain its
        own character (like line breaks with ``%``). Nothing has been
        confirmed yet, so keep up to date with the documentation.

^^^^^^^^^^^^^^^^^^^^
Decoding Identifiers
^^^^^^^^^^^^^^^^^^^^

The following characters will appear by themselves, and they have literal
translations which are easy to convert to:

- ``%`` -> ``[LINE BREAK]``
- ``,`` -> ``[SPACE]``

Decoding Waves
==============

Decoding each wave is just like encoding, but in reverse! There are two good
ways to do this, see which one fits you the best:

^^^^^^^^^^
Wave boxes
^^^^^^^^^^

For this, you will need the image of the boxes - or you can draw it out yourself.

.. csv-table::
   :file: /tables/all.csv
   :widths: 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
   :align: center

Imagine a random wave: ``_>o``. We can see that this wave has an **o** at the end,
this means it will be in the fourth box.

.. csv-table::
   :file: /tables/t4.csv
   :widths: 2 2 2 2 2
   :align: left

The first character (``_``), our row indicator, indicates that its at the bottom.
As we can see on our table, it would be the bottom row, which only consists of "7",
"8" and "9". Now we refer to the second character (``>``), our column indicator,
which shows us its the character on the right. This means ``_>o`` in oceanscript
would be the number 9.

^^^^^^^^^
Wave sets
^^^^^^^^^

Group the alphabet (merged with 0-9 onto the end) into sets of 9.
You should end up with the following:

- ``abcdefghi``
- ``jklmnopqr``
- ``stuvwxyz0``
- ``123456789``

This is essentially our boxes, but grouped into lines or "sets" instead.

Now imagine you are given a completely random wave, ``~<..``. You can see its got
**2** dots, so it is going to be in the **2**nd set.

.. code-block:: diff

    - abcdefghi
    + jklmnopqr
    - stuvwxyz0
    - 123456789

You can see that the first character is ``~`` - remember, the first character indicates
the **row**. Its indicating the second row, so its going to be the second yield of 3
characters in this set we have.

.. code-block:: diff

    - jkl
    + mno
    - pqr

The second character is ``<``, which points to the left. Our wave ``~<..`` is "m"!

.. code-block:: diff

    + m
    - n
    - o

Tips & Advice
=============

I, the writer of this document, had obviously thought up the concepts and ideas of
oceanscript - therefore all the decoding happens inside my head inside of needing to
have a visual representation of boxes or sets.

One thing I found useful was remembering characters in sets of 3, for example "abc",
"mno", "stu". This helps to nullify that time taken to think about which row and column
your letter is in, as you eventually accustomize to these sets of 3 quite nicely.

When decoding, you also need to remember what each indicator means - but the indicators
were picked with some sense which makes them easier to remember - they aren't just random
characters. The row indicators, ``^`` is an arrow pointing UP, so its on the TOP row, ``~``
hangs in the middle and ``_`` is on the floor (bottom row). The column indicators are even
easier with ``<`` and ``>``.

If you plan to learn to decode without the use of the Python decoder, then good luck to you!
Feel free to reach out to me letting me know how you are getting on with it.
