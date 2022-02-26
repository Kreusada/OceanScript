.. _api-decoding:

Decoding OceanScript
====================

Use the :func:`~oceanscript.decode` function.

.. warning::

    If the oceanscript is not valid, :class:`~oceanscript.OceanScriptError`
    will be raised! See more about error handling :ref:`here <api-error_handling>`

^^^^^^^^^^^^^
Example Usage
^^^^^^^^^^^^^

.. code-block:: python

    >>> text = '^<....=.,*^-.^<.^>.~>..~-..%^-....=.,*~-._<._<.^<...%^>....=.,*_-.^<.~<..'
    >>> oceanscript.decode(text)
    '1. Bacon'
    '2. Eggs'
    '3. Ham'

    >>> text = '*_-.~-.^>..^>..~>..\n~<.._<...\n~-..^<.~<..~-.\n_>.^<...\n*^-.._>..~-.^>...^<...^<.~<.^<.=!'
    >>> oceanscript.decode(text)
    'Hello my name is Kreusada!'
