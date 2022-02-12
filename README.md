<h1 align="center">
  <br>
  <a href="https://github.com/Kreusada/OceanScript"><img src="https://github.com/Kreusada/OceanScript/blob/main/.github/oceanscript.png?raw=true" alt="OceanScript Esoteric Language"></a>
  <br>
  OceanScript Esoteric Language
  <br>
</h1>

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://user-images.githubusercontent.com/6032823/111363465-600fe880-8690-11eb-8377-ec1d4d5ff981.png)](https://github.com/PyCQA/isort)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

# Overview

OceanScript is an Esoteric language used to encode and decode text into
a formulation of characters - where the final result looks like waves in the ocean.

Unlike it's prior versions, OceanScript supports any character, as well as capitalization.
Your encoded string should be decoded to look exactly the same as the encoded string. Note, however,
that outlying whitespace characters are stripped from the edges of the text.

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
`^` | 1 | 2 | 3 | `....`
`~` | 4 | 5 | 6 | `....`
`_` | 7 | 8 | 9 | `....`
ㅤ | `<` | `-` | `>` |ㅤ

When typing a character, you need to check the following in order:

* What row is my character in?
* What column is my character in?
* What box is my character in?

* The rows are denoted by the following characters: `^`, `~`, `_`.
* The columns are denoted by the following indicators: `<`, `-`, `>`.
* The boxes are denoted by `.`, multipled by n, where n is the box number. There are 4 boxes.

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

Using the table above, the character `a` is in the top row of it's box,
so our first character is `^`. Next, you need to check the column. `a` is
also in the first column, so our second character is `<` (pointing to the left).
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

Using the table above, the character `x` is in the second row of it's box,
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
Greek lambda character (`λ`), it will need a raft seeing as its not in the large table,
so it would simply be written as `=λ`. More common characters (`.`, `!`, `?`) are more likely
to appear, they will need rafts too.

* `?` -> `=?`
* `^` -> `=^`
* `...` -> `=.=.=.`

Despite not appearing in the table, capitalized a-z characters **DO NOT** need to use rafts.
See below about capitalization.

## Capitalization

Capitalization hadn't been supported for months proceeding the initial release
of oceanscript, but its now available. To make a character capital, use a splash (`*`) before the wave.

* `a` -> `^<.`
* `A` -> `*<.`

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
`,` | Represents a space
`\n` | Represents a space
`%` | Represents a line break
`=` | Creates a raft for a single character (proceeding character will be ignored by encoder)
`*` | Creates a splash for a wave (proceeding wave will be capitalized)
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
`wave` | A single character encoded into oceanscript. | `^<..`
`tide` | A collection of waves to form a word, where the word is the tide. | `*_-.~-.^>..^>..~>..`
`raft` | A character (`=`) used to prefix a special character (not a-Z or 0-9). | `=.`
`splash` | A character (`*`) used to capitalize the following wave. | `*_<.`

# Python Implementation

As a programmer, I just had to make a Python library for this.
Once upon a time, it was all just a looming thought in my mind with so much
potential. Its been great to be able to create a working usable program for it,
for anyone to use and play around with.

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
exception was raised (at the start of the wave).

```py
>>> oceanscript.decode("*>....") # capitalizing int
OceanScriptError: Capitalization indicator not allowed for integers (position 0)

>>> oceanscript.decode("=a") # rafting ascii value
OceanScriptError: Do not escape ascii letters/digits in escape sequence ('=a'). Use '^<.' instead. (position 0)

>>> oceanscript.decode("^-.~>..#>..") # invalid row indicator '#'
OceanScriptError: '#' is not a valid row indicator (position 7)

>>> oceanscript.decode("^+...") # invalid column indicator '+'
OceanScriptError: '^' marker expected '<', '-', or '>', but received '+' instead (position 0)
```

Other tracebacks can appear, too.

# Installation

Install from the recommended package installer, **pip**.

```sh
pip install oceanscript
```

# License

Licensed under MIT.
