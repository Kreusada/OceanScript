"""
OceanScript is an Esoteric language used to encode and decode text
into a formulation of characters - where the final result looks like waves in the ocean.
"""

import re
import string
from typing import Literal, Optional, Tuple

__all__ = (
    "OceanScriptError",
    "decode",
    "encode",
)

__version__ = "2.3.0"

ROW_INDICATORS = "^~_"
COLUMN_INDICATORS = "<->"
R1S = "abcjklstu123"
R2S = "defmnovwx456"
R3S = "ghipqryz0789"
R1S1S = "ajs1"
R1S2S = "bkt2"
R1S3S = "clu3"
R2S1S = "dmv4"
R2S2S = "enw5"
R2S3S = "fox6"
R3S1S = "gpy7"
R3S2S = "hqz8"
R3S3S = "ir09"

DOT_INDEX_MAPPING = {
    0: ".",
    1: ".",
    2: ".",
    3: "..",
    4: "..",
    5: "..",
    6: "...",
    7: "...",
    8: "...",
    # 9, 10, 11 shall use "o" instead of "...."
    # for the future. When encoding "3" for example,
    # it will return "^>o" instead of "^>...." as of 2.3.0.
    # 4-dot syntax is still permittable but may be
    # slated for deprecation and removal in the far
    # distant future. Its in my best recommendations
    # to begin getting used to this newer syntax.
    9: "o",
    10: "o",
    11: "o",
}


class OceanScriptError(Exception):
    """Exception class used to raise decoding errors."""

    def __init__(self, *, message: str, position: Optional[int] = None) -> None:
        self.position = position
        self._message = message
        if position is not None:
            message = f"[Position {position}] " + message
        super().__init__(message)

    def without_position_reference(self) -> str:
        """Returns the traceback string without the position reference at the end.

        Returns
        ------
        str
            The traceback message without position reference.
        """
        return self._message


def encode(text: str, *, mode: Optional[Literal["squash", "stretch"]] = "squash") -> str:
    """Encode text into oceanscript.

    Parameters
    ----------

    text: str
        The text to encode into oceanscript.

    mode: Optional[Literal["squash", "stretch"]] = "squash"
        The mode used to encode the oceanscript.

        Use 'squash' to replace spaces with commas.
        Use 'stretch' to replace spaces with line breaks.

    Returns
    -------
    str
        The oceanscript.
    """
    ret = ""
    for char in text:
        if char.isupper():
            # capitals in oceanscript use the splash indicator (*)
            # before wave declaration
            ret += "*"
        # now that potential capitalization has been recorded, we will
        # convert the character to lower case. This is to make encoding
        # faster and easier, but also prevents errors with capitalized
        # alphabetic characters after the splash indicator i.e.
        # "*=λ" is allowed but "*=Λ" is not
        char = char.lower()
        if char in R1S:
            ret += "^"
            if char in R1S1S:
                ret += "<"
            elif char in R1S2S:
                ret += "-"
            else:
                ret += ">"
            ret += DOT_INDEX_MAPPING[R1S.index(char)]
        elif char in R2S:
            ret += "~"
            if char in R2S1S:
                ret += "<"
            elif char in R2S2S:
                ret += "-"
            else:
                ret += ">"
            ret += DOT_INDEX_MAPPING[R2S.index(char)]
        elif char in R3S:
            ret += "_"
            if char in R3S1S:
                ret += "<"
            elif char in R3S2S:
                ret += "-"
            else:
                ret += ">"
            ret += DOT_INDEX_MAPPING[R3S.index(char)]
        elif char == " ":
            if mode == "squash":
                # squash mode ensures that no whitespace characters
                # are found in the encoding
                ret += ","
            elif mode == "stretch":
                # stretch mode ensures a line break splits each wave
                ret += "\n"
            else:
                raise ValueError(f"unknown mode '{mode}'")
        elif char == "\n":
            # % is used to represent line breaks in oceanscript
            ret += "%"
        else:
            # now we've covered all the special and default scenarios,
            # this character requires a raft. Rafts are used to support
            # any other characters that are not handled above
            ret += "=" + char
    return ret


def splitwaves(text: str, *, include_invalid: bool = True) -> Tuple[str]:
    """Split oceanscript into waves.

    Invalid characters will not be omitted from the returned tuple.

    Parameters
    ----------

    text: str
        The oceanscript to split.

    include_invalid: bool
        Whether to include invalid identifiers in the string.
        Defaults to True.

    Returns
    -------

    Tuple[str]
        A tuple of waves split from the oceanscript
    """
    split = re.split(r"(\*?=.)|(\\n|,|%)|(\*?[\^~_][>\-<](?:\.+|o))|(.|\n)", text)
    if include_invalid:
        check = None
    else:
        # all invalid identifiers are isolated as length 1 strings
        check = lambda e: e and (e in "\n,%" or len(e) != 1)
    return tuple(filter(check, split))


def decode(text: str) -> str:
    """Decode oceanscript into text.

    Parameters
    ----------

    text: str
        The oceanscript to decode into text.

    Returns
    -------
    str
        The original text.
    """
    chunks = splitwaves(text)  # this is now a public method
    ret = ""
    for i, s in enumerate(chunks):
        position = sum(map(len, chunks[:i]))
        # this position variable is the index of the first
        # character of this current iteration inside the entire string
        if s in ",\n":
            ret += " "
            continue
        if s == "%":
            ret += "\n"
            continue
        if len(s) == 1:
            # thanks to the regex, any invalid identifier will be isolated
            # as an element with a length of 1

            # here, i am just finelining the traceback message to make it
            # much clearer for the user where they went wrong
            if s == "=":
                message = "Raft deployed without passenger"
            elif s == "*":
                message = "Splash created without wave declaration"
            elif s in ROW_INDICATORS:
                message = f"Row indicator '{s}' expecting valid column indicator afterwards ('<', '-', or '>')"
            elif s in COLUMN_INDICATORS:
                message = f"Waves must start with row indicators, not a column indicator ('{s}'). Expecting valid row indicator instead ('^', '~', or '_')"
            elif s == ".":
                message = "Dot indicator expecting to follow partially established waves, but do not follow any partial wave at this position"
            elif s in string.ascii_letters + string.digits:
                message = f"Invalid syntax: '{s}'. Ascii letters and integers must be written in their encoded form ({s} = '{encode(s)}')."
                if position == 0:
                    # start of the string, wrong method used, so this logical suggestion is made
                    message += " Perhaps you were meant to use oceanscript.encode()?"
            elif s == " ":
                message = f"Invalid syntax: '{s}'. Perhaps you meant ','?"
            else:
                # just like encoding the string, passing through other scenarios
                # has left us nowhere. This is an invalid character, so we will
                # suggest to prefix it with a raft
                message = f"Invalid syntax: '{s}'. Perhaps you meant '={s}'?"

            raise OceanScriptError(
                message=message,
                position=position,
            )

        if s[0] == "*":
            s = s[1:]
            try:
                # this is being done because the
                # splash indicator should only be used on alphabetic
                # waves. we can't just check if an iterable of strings
                # contains a-z, because greek (for example) letters
                # need to be taken into consideration
                # i.e.: "*=δ" but NOT "*=["
                d = decode("".join(s))
            except OceanScriptError:
                # this will be handled with its full string
                pass
            else:
                if d.isdigit():
                    raise OceanScriptError(
                        message="Splash indicator not allowed for integer waves", position=position
                    )
                if not d.isalpha():
                    raise OceanScriptError(
                        message="Splash indicator only allowed for alphabetic waves",
                        position=position,
                    )
                if d.isupper():
                    raise OceanScriptError(
                        message=(
                            f"Splash is redundent in this position, given wave is already uppercase ('{d}'). "
                            f"Use '*={d.lower()}' or '={d}' instead."
                        ),
                        position=position,
                    )
            # splash indicator means the string in this iteration
            # must be capitalized. For the sake of ease, an inutile
            # lambda will otherwise call the string
            func = str.upper
        else:
            func = lambda x: x

        if s[0] == "=":
            after = "".join(s[1:])
            for character in string.ascii_letters + string.digits:
                if character in after:
                    # a-Z/0-9 are the only characters where a raft
                    # cannot be used
                    raise OceanScriptError(
                        message=f"Do not use a-Z/0-9 on a raft ('={character}'). Use '{encode(character)}' instead.",
                        position=position,
                    )
            ret += func(after)
            continue

        row_indicator = s[0]
        if row_indicator not in ROW_INDICATORS:
            raise OceanScriptError(
                message=f"Expected '^', '~', or '_' as a row indicator, but received '{row_indicator}' instead",
                position=position,
            )
        column_indicator = s[1]
        if column_indicator not in COLUMN_INDICATORS:
            raise OceanScriptError(
                message=f"Row indicator '{row_indicator}' expected '<', '-', or '>', but received '{column_indicator}' instead",
                position=position,
            )
        dots = s[2:]
        # <row_indicator><column_indicator><dots...> (2:)
        cdots = len(dots)
        dot_range = range(1, 5)  # double reference
        if cdots not in dot_range:
            if cdots == 0:
                m = "but did not find anything at this position"
            else:
                m = f"but found {cdots} dots instead"
            raise OceanScriptError(
                message=f"Partially established wave ('{row_indicator}{column_indicator}') expected 1, 2, 3, or 4 dots (or 4 dot notation 'o') at the end, {m}",
                position=position,
            )
        if not all(map("o.".__contains__, dots)):
            raise OceanScriptError(
                message=f"'{column_indicator}' indicator expected only dot indicators, or the 4 dot notation 'o', but received '{dots}' instead",
                position=position,
            )
        if dots == "o":
            # "o" syntax needs to always be recognized as a count
            # of 4 dots under the hood for this next process to work
            # properly. Without this, decoded integers would instead
            # be translated to a-i in the first box.
            cdots = 4
        if row_indicator == "^":
            if column_indicator == "<":
                selection = R1S1S
            elif column_indicator == "-":
                selection = R1S2S
            else:
                selection = R1S3S
        elif row_indicator == "~":
            if column_indicator == "<":
                selection = R2S1S
            elif column_indicator == "-":
                selection = R2S2S
            else:
                selection = R2S3S
        else:
            if column_indicator == "<":
                selection = R3S1S
            elif column_indicator == "-":
                selection = R3S2S
            else:
                selection = R3S3S
        letters = dict(zip(dot_range, selection))
        ret += func(letters[cdots])
    return ret
