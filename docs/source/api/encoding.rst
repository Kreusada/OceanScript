.. _api-encoding:

Encoding OceanScript
====================

Use the :func:`~oceanscript.encode` function.

In this function, there is an optional keyword-only argument named "mode",
which can be one of "stretch" or "squash" - defaulting to "squash".

.. _api-encoding-mode-stretch:

^^^^^^^^^^^^
Stretch mode
^^^^^^^^^^^^

Replaces instances of whitespace (" ") with line breaks. This mode is handy
for encoding mass amounts of text, or to present oceanscript nicely.

.. code-block:: python

    >>> oceanscript.encode('Hello world!', mode='stretch')
    '*_-.~-.^>..^>..~>..'
    '~-...~>.._>..^>..~<.=!'

.. _api-encoding-mode-squash:

^^^^^^^^^^^
Squash mode
^^^^^^^^^^^

Replaces instances of whitespace (" ") with commas. This mode is handy
for shorter amounts of text to fit on single lines.

.. code-block:: python

    >>> oceanscript.encode('Hello world!', mode='squash')
    '*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!'

.. _api-encoding-examples:

^^^^^^^^^^^^^
Example Usage
^^^^^^^^^^^^^

.. code-block:: python

    >>> text = '1. Bacon\n2. Eggs\n3. Ham'
    >>> oceanscript.encode(text)
    '^<....=.,*^-.^<.^>.~>..~-..%^-....=.,*~-._<._<.^<...%^>....=.,*_-.^<.~<..'

    >>> text = 'Hello my name is Kreusada!'
    >>> oceanscript.encode(text, mode='stretch')
    '*_-.~-.^>..^>..~>..'
    '~<.._<...'
    '~-..^<.~<..~-.'
    '_>.^<...'
    '*^-.._>..~-.^>...^<...^<.~<.^<.=!'
