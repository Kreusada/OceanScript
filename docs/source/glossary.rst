.. _glossary:

.. _glossary-terminology:

^^^^^^^^^^^^^^^^^^^
Terminology Glossary
^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 50
    :header-rows: 1

    * - Word
      - Meaning
      - Example
    * - Raft
      - A character (``=``) used to prefix a special character (not a-Z or 0-9).
      - ``=.``
    * - Ripple
      - A character that would make up a **wave**.
      - ``^``
    * - Splash
      - A character (``*``) used to capitalize the following wave.
      - ``*_<.``
    * - Tide
      - A collection of waves to form a word, where the word is the tide.
      - ``*_-.~-.^>..^>..~>..``
    * - Wave
      - A single character encoded into oceanscript.
      - ``^<..``

.. _glossary-identifier:

^^^^^^^^^^^^^^^^^^^
Identifier Glossary
^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 15 50 10
    :header-rows: 1

    * - Identifier
      - Description
    * - ``,``
      - Represents a space.
    * - ``\n``
      - Represents a space.
    * - ``%``
      - Represents a line break.
    * - ``=``
      - Creates a raft for a single character (proceeding character will be ignored by encoder).
    * - ``*``
      - Creates a splash for a wave (proceeding wave will be capitalized).
    * - ``^``
      - Denotes the top row of a box for a single wave.
    * - ``~``
      - Denotes the middle row of a box for a single wave.
    * - ``_``
      - Denotes the bottom row of a box for a single wave.
    * - ``<``
      - Denotes the left-hand column of a box for a single wave.
    * - ``-``
      - Denotes the central column of a box for a single wave.
    * - ``>``
      - Denotes the right-hand column of a box for a single wave.
    * - ``.``
      - Denotes the box number based on the count of this character. Must be 1-3.
    * - ``o``
      - Denotes the 4th box.
