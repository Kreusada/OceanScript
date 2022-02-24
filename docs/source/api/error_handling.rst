.. _api-error_handling:

Error Handling
==============

Decoding oceanscript may raise errors dependent on the input you provide.
If the oceanscript isn't valid, it will raise :class:`~oceanscript.OceanScriptError`
with the details needed to fix the issue.

.. _api-error_handling-position_attribute:

^^^^^^^^^^^^^^^^^^^^^^^^^^
Expansive traceback detail
^^^^^^^^^^^^^^^^^^^^^^^^^^

The tracebacks are detailed and specific, take a look at these examples:

.. code-block:: python

    >>> oceanscript.decode("*^>o") # trying to capitalize integer (3)
    OceanScriptError: [Position 0] Splash indicator not allowed for integer waves

    >>> oceanscript.decode("=a") # rafting a-Z/0-9
    OceanScriptError: [Position 0] Do not use a-Z/0-9 on a raft ('=a'). Use '^<.' instead.

    >>> oceanscript.decode("^-.~>..#>..") # invalid row indicator '#'
    OceanScriptError: [Position 7] Invalid syntax: '#'. Perhaps you meant '=#'?

    >>> oceanscript.decode("*^-..._>._-.^<...,_>.^<...,~-..._>..~>..~-.._+.") # invalid column indicator '+'
    OceanScriptError: [Position 44] Row indicator '_' expecting valid column indicator afterwards ('<', '-', or '>')

    >>> oceanscript.encode("*~<.~-.^>..^-...^<.=:,*=Δ") # splash indicator before already capitalized alphabetic character
    OceanScriptError: [Position 22] Splash is redundent in this position, given wave is already uppercase ('Δ'). Use '*=δ' or '=Δ' instead.

^^^^^^^^^^^^^^^^^^
Position attribute
^^^^^^^^^^^^^^^^^^

Each exception has a ``position`` attribute, which contains the string index
of the start of the wave which errored whilst parsing. For example:

.. code-block:: python

    >>> try:
    ...     oceanscript.decode("*_-._>.!")
    ... except oceanscript.OceanScriptError as err:
    ...     print(err.position)
    7

``!`` is not a-Z/0-9, so it needs a raft. At position 7, it should be ``=!``,
not ``!``. The position indication can be helpful for resolving these mistakes.

.. _api-error_handling-without_position_reference_method:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Position reference omission method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This method (:meth:`~oceanscript.OceanScriptError.without_position_reference`) will
show tracebacks without the position reference prefixed to the start of the traceback string.

.. code-block:: python

    >>> try:
    ...     oceanscript.decode("*")
    ... except oceanscript.OceanScriptError as err:
    ...     print(err)
    '[Position 0] Splash created without wave declaration'
    >>> print(err.without_position_reference())
    'Splash created without wave declaration'
