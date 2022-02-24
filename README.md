<h1 align="center">
  <br>
  <a href="https://github.com/Kreusada/OceanScript"><img src="https://github.com/Kreusada/OceanScript/blob/main/.github/oceanscript.png?raw=true" alt="OceanScript Esoteric Language"></a>
  <br>
  OceanScript Esoteric Language (2.3.0 release)
  <br>
</h1>

<p align="center">
  <a href="https://github.com/psf/black">
    <img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://github.com/PyCQA/isort">
     <img alt="Imports: Isort" src="https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png">
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Versions" src="https://img.shields.io/pypi/pyversions/OceanScript">
  </a>
  <a href="https://www.patreon.com/kreusada">
    <img src="https://img.shields.io/badge/Support-on%20Patreon-red.svg" alt="Support on Patreon">
  </a>
</p>

<p align="center">
  <a href="https://pepy.tech/project/oceanscript">
    <img alt="Total downloads" src="https://pepy.tech/badge/oceanscript">
  </a>
  <a href="https://pepy.tech/project/oceanscript">
    <img alt="Downloads in the past month" src="https://pepy.tech/badge/oceanscript/month">
  </a>
  <a href="https://pepy.tech/project/oceanscript">
    <img alt="Downloads in the past week" src="https://pepy.tech/badge/oceanscript/week">
  </a>
</p>

# Overview

OceanScript is an Esoteric language used to encode and decode text into
a formulation of characters - where the final result looks like waves in the ocean.

Unlike its prior versions, OceanScript supports any character, as well as capitalization.
Your encoded string should be decoded to look exactly the same as the encoded string.

# How does it work?

OceanScript isn't just random choice or a random jumble of characters. These characters
have very specific meanings, which once understood, can be used to write oceanscript
without the use of the encoder. Take a look at these 4 tables below:

ㅤ | `<` | `-` | `>` |ㅤ
--- | --- | --- | --- | ---
`^` | a | b | c | `.`
`~` | d | e | f | `.`
`_` | g | h | i | `.`
ㅤ | `<` | `-` | `>`
`^` | j | k | l | `..`
`~` | m | n | o | `..`
`_` | p | q | r | `..`
ㅤ | `<` | `-` | `>` |ㅤ
`^` | s | t | u | `...`
`~` | v | w | x | `...`
`_` | y | z | 0 | `...`
ㅤ | `<` | `-` | `>` |ㅤ
`^` | 1 | 2 | 3 | `o`
`~` | 4 | 5 | 6 | `o`
`_` | 7 | 8 | 9 | `o`
ㅤ | `<` | `-` | `>` |ㅤ

When typing a character, you need to check the following in order:

* What row is my character in? (The rows are denoted by the following characters: `^`, `~`, `_`.)
* What column is my character in? (The columns are denoted by the following indicators: `<`, `-`, `>`.)
* What box is my character in? (The boxes are denoted by `.`, multipled by n, where n is the box number. There are 4 boxes.)

**Warning**

  As of v2.3.0, BOX-4 characters (1-9) use `o` instead of `....` for box denotion.
  Please adjust to using this syntax as soon as possible.

Our final product will be known as a "wave". It will contain from 3 to 6 characters.
Have a look at some examples below to understand how to write these waves.

### Exemplar `a`

Here is an example of typing the character `a`. It is the easiest character to type
from memory, and is great to use as a first example. Lets zoom in on `a`'s box below:

ㅤ | `<` | `-` | `>` |ㅤ
--- | --- | --- | --- | ---
`^` | a | b | c | `.`
`~` | d | e | f | `.`
`_` | g | h | i | `.`
ㅤ | `<` | `-` | `>` |ㅤ

Using the table above, the character `a` is in the top row of its box,
so our first character is `^`. Next, you need to check the column. `a` is
in the left-hand column, so our second character is `<` (pointing to the left).
Finally, we need to check which box character `a` is in. We will add `.` according to
the table above. The number of dots corresponds to the box number (1-4).

`a` in oceanscript is `^<.`.

### Exemplar `x`

Here is an example of typing the character `x`. Lets zoom in on `x`'s box below:

ㅤ | `<` | `-` | `>` |ㅤ
--- | --- | --- | --- | ---
`^` | s | t | u | `...`
`~` | v | w | x | `...`
`_` | y | z | 0 | `...`
ㅤ | `<` | `-` | `>` |ㅤ

Using the table above, the character `x` is in the second row of its box,
so our first character is `~`. Next, you need to check the column. `x` is
in the right-hand column, so our second character is `>` (pointing to the right).
Finally, we need to check which box character `x` is in. We will add `...`, because
this is box 3 of 4.

`x` in oceanscript is `~>...`.

### Joining waves

Wave is the name used for a single encoded character (`z` -> `_-...`). Waves can be freely
joined together. Remember that every character ends with `.`, so you can easily work out where
each wave ends.

* `hello` -> `_-.~-.^>..^>..~>..`
* `foobar` -> `~>.~>..~>..^-.^<._>..`

### Joining tides

Tide is the name used for a collection of "waves", so essentially a word converted
into oceanscript. For example, `_-.~-.^>..^>..~>..` is a tide, meaning "hello".
Tides can be joined using either commas, or line breaks. For pretty formatting, or if
you have a lot of text, you should use line breaks - but otherwise go with commas.

* `hello foobar` -> `_-.~-.^>..^>..~>..,~>.~>..~>..^-.^<._>..`
(notice the comma separating these two waves)

**OR...**

* `hello foobar` ->

  `_-.~-.^>..^>..~>..`

  `~>.~>..~>..^-.^<._>..`

## Special characters

Don't fear, oceanscript isn't just limited to a-z and 0-9. Well, it used to be - but a
new special character indicator has been added to support any other character.

It is best to keep these special characters out of the ocean, so these characters will
need to use a raft (`=`). Simply put the raft before the character. If you wanted to write the
Greek lambda character (`λ`), it will need a raft seeing as it's not in the large table,
so it would simply be written as `=λ`. More common characters (`.`, `!`, `?`) are more likely
to appear, they will need rafts too.

* `?` -> `=?`
* `^` -> `=^`
* `...` -> `=.=.=.`

Despite not appearing in the table, capitalized a-z characters **DO NOT** need to use rafts.
See below about capitalization.

## Capitalization

Capitalization hadn't been supported for months proceeding the initial release
of oceanscript, but it's now available. To make a character capital, use a splash (`*`) before the wave.

* `a` -> `^<.`
* `A` -> `*^<.`

For each capital wave you have, you will have to add a splash before each one. *Yes, these waves are choppy...*

* `hello` -> `_-.~-.^>..^>..~>..`
* `HELLO` -> `*_-.*~-.*^>..*^>..*~>..`

Note that you should not use splashes for numeric characters, or any characters that are not alphabetic.
This is because these characters do not have case forms (and therefore don't produce splashes! *You could call them subtle waves...*)

## Line breaks

For line breaks in oceanscript, use `%`. For example, presenting an acronym:

```
N
A
S
A
```

In oceanscript, the above acronym would be encoded into `*~-..%*^<.%*^<...%*^<.`.

## All identifiers

Identifier | Description
--- | ---
`,` | Represents a space.
`\n` | Represents a space.
`%` | Represents a line break.
`=` | Creates a raft for a single character (proceeding character will be ignored by encoder).
`*` | Creates a splash for a wave (proceeding wave will be capitalized).
`^` | Denotes the top row of a box for a single wave.
`~` | Denotes the middle row of a box for a single wave.
`_` | Denotes the bottom row of a box for a single wave.
`<` | Denotes the left-handed column of a box for a single wave.
`-` | Denotes the central column of a box for a single wave.
`>` | Denotes the right-handed column of a box for a single wave.
`.` | Denotes the box number based on the count of ".".

## Terminology glossary

Word | Description | Example
--- | --- | ---
`raft` | A character (`=`) used to prefix a special character (not a-Z or 0-9). | `=.`
`ripple` | A character that would make up a wave. Does not include `=`, `*` or `%`. | `^`
`splash` | A character (`*`) used to capitalize the following wave. | `*_<.`
`tide` | A collection of waves to form a word, where the word is the tide. | `*_-.~-.^>..^>..~>..`
`wave` | A single character encoded into oceanscript. | `^<..`


# Python Implementation

I just had to make a Python library for this. It was all just a looming thought
in my mind with so much potential. It's been great to be able to create a working
usable program for it, for anyone to use and play around with.

Start by importing the module:

```py
import oceanscript
```

### Encoding into oceanscript

Use the `oceanscript.encode` method. This method also takes an optional
keyword-only argument "mode", which decides whether the encoder uses commas
or line breaks to replace spaces. Specify `stretch` for line breaks, or
`squash` for commas. Defaults to `squash`.

```py
>>> oceanscript.encode("hello")
'_-.~-.^>..^>..~>..'

>>> oceanscript.encode("Hello world!")
'*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!'

>>> oceanscript.encode("Hello world!", mode="stretch")
'*_-.~-.^>..^>..~>..'
'~-...~>.._>..^>..~<.=!'
```

### Decoding from oceanscript

Use the `oceanscript.decode` method. Both modes from the encode method are
compatible with decoding (you don't have to specify a mode here).

```py
>>> oceanscript.decode("_-.~-.^>..^>..~>..")
'hello'

>>> oceanscript.decode("*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!")
'Hello world!'

>>> text = """
    *_-.~-.^>..^>..~>..
    ~-...~>.._>..^>..~<.=!
    """
>>> oceanscript.decode(text)
'Hello world!'
```

If the oceanscript doesn't look quite right, the parser won't like it.
`oceanscript.OceanScriptError` is thrown, but the traceback details are fairly useful
for correcting these mistakes.

OceanScriptError has a `position` attribute, which is the string index in where the
exception was raised (at the start of the wave affected).

```py
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
```

Other tracebacks can appear, too.

You can handle tracebacks to your own liking with the `.without_position_reference()` method
to remove the position reference prefixed to the start of the exception string.

```py
>>> try:
...     oceanscript.decode("*~>.._<.~>..~-..~-.^-..,*~>..=:,*=Ǫ")
... except OceanScriptError as err:
...     print(err.without_position_reference())
"Splash is redundent in this position, given wave is already uppercase ('Ǫ'). Use '*=ǫ' or '=Ǫ' instead."
```

### Splitting Waves

Since `v2.1.0`, the functionality to split waves has been created as
a public method, and is continually used by the decoder when decoding.
It has an `include_invalid` keyword only argument which defines whether
to include invalid identifiers/waves in the string, defaulting to True.

```py
>>> oceanscript.splitwaves("*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!")
('*_-.', '~-.', '^>..', '^>..', '~>..', ',', '~-...', '~>..', '_>..', '^>..', '~<.', '=!')
>>> oceanscript.splitwaves("*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!,bad")
('*_-.', '~-.', '^>..', '^>..', '~>..', ',', '~-...', '~>..', '_>..', '^>..', '~<.', '=!', ',', 'b', 'a', 'd')
>>> oceanscript.splitwaves("*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!,bad", include_invalid=False)
('*_-.', '~-.', '^>..', '^>..', '~>..', ',', '~-...', '~>..', '_>..', '^>..', '~<.', '=!', ',')
```

# Installation

Install from the recommended package installer, **pip**.

```sh
pip install oceanscript
```

# License

Licensed under MIT.
