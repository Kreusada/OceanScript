"""
OceanScript is an Esoteric language used to encode and decode text
into a formulation of characters - where the final result looks like waves in the ocean.
"""

import re
import string
from typing import Literal, Optional

__all__ = (
    "OceanScriptError",
    "decode",
    "encode",
)

__version__ = "2.0.2"

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

MUL_MAPPING = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 3,
    7: 3,
    8: 3,
    9: 4,
    10: 4,
    11: 4,
}


class OceanScriptError(Exception):
    """Exception class used to raise decoding errors."""

    def __init__(self, *, message: str, position: int) -> None:
        self.position = position
        super().__init__(f"{message} (position {position})")


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
    for char in text.strip():
        if char.isupper():
            ret += "*"
        char = char.lower()
        if char in R1S:
            ret += "^"
            if char in R1S1S:
                ret += "<"
            elif char in R1S2S:
                ret += "-"
            else:
                ret += ">"
            ret += "." * MUL_MAPPING[R1S.index(char)]
        elif char in R2S:
            ret += "~"
            if char in R2S1S:
                ret += "<"
            elif char in R2S2S:
                ret += "-"
            else:
                ret += ">"
            ret += "." * MUL_MAPPING[R2S.index(char)]
        elif char in R3S:
            ret += "_"
            if char in R3S1S:
                ret += "<"
            elif char in R3S2S:
                ret += "-"
            else:
                ret += ">"
            ret += "." * MUL_MAPPING[R3S.index(char)]
        elif char == " ":
            if mode == "squash":
                ret += ","
            elif mode == "stretch":
                ret += "\n"
            else:
                raise ValueError(f"unknown mode '{mode}'")
        elif char == "\n":
            ret += "%"
        else:
            ret += "=" + char
    return ret


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
    split = re.split(r"(\*?=.)|(\\n|,|%)|(\*?[\^~_][>\-<]\.{1,4})", text.strip())
    ret = tuple(filter(None, split))
    message = ""
    for i, s in enumerate(ret):
        position = sum(map(len, ret[:i]))
        if s in ",\n":
            message += " "
            continue
        if s == "%":
            message += "\n"
            continue
        if len(s) < 2:
            raise OceanScriptError(
                message=f"invalid syntax '{s}'",
                position=position,
            )

        if s[0] == "*":
            s = s[1:]
            join = "".join(s)
            if join in (
                "_>...",
                "^<....",
                "^-....",
                "^>....",
                "~<....",
                "~-....",
                "~>....",
                "_<....",
                "_-....",
                "_>....",
            ):
                raise OceanScriptError(
                    message="Splash indicator not allowed for integers",
                    position=position,
                )
            func = str.upper
        else:
            func = lambda x: x

        if s[0] == "=":
            after = "".join(s[1:])
            for letter in string.ascii_letters + string.digits:
                if letter in after:
                    raise OceanScriptError(
                        message=f"Do not use lowercase ascii letters or digits on a raft ('={letter}'). Use '{encode(letter)}' instead.",
                        position=position,
                    )
            message += func(after)
            continue

        row_indicator = s[0]
        if row_indicator not in ROW_INDICATORS:
            raise OceanScriptError(
                message=f"'{row_indicator}' is not a valid row indicator",
                position=position,
            )
        column_indicator = s[1]
        if column_indicator not in COLUMN_INDICATORS:
            raise OceanScriptError(
                message=f"'{row_indicator}' indicator expected '<', '-', or '>', but received '{column_indicator}' instead",
                position=position,
            )
        dots = s[2:]
        cdots = len(dots)
        if cdots not in range(1, 5):
            raise OceanScriptError(
                message=f"Expected 1, 2, 3 or 4 dots, but found {cdots} instead",
                position=position,
            )
        if any(d != "." for d in dots):
            raise OceanScriptError(
                message=f"'{column_indicator}' indicator expected only dots, but received '{dots}' instead",
                position=position,
            )
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
        letters = dict(zip(range(1, 5), selection))
        message += func(letters[cdots])
        continue
    return message
