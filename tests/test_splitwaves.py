import unittest

from oceanscript import splitwaves

BAD = "bad"
FALSY_HELLO_WORLD = "*_-.~-.^>..^>..~>..,~-...~>.._>..^>..~<.=!," + BAD
EXPECTED_SPLIT = (
    "*_-.",
    "~-.",
    "^>..",
    "^>..",
    "~>..",
    ",",
    "~-...",
    "~>..",
    "_>..",
    "^>..",
    "~<.",
    "=!",
    ",",
    "b",
    "a",
    "d",
)


class TestSplitWaves(unittest.TestCase):
    def test_splitwaves_include_invalid(self):
        split = splitwaves(FALSY_HELLO_WORLD)
        self.assertEqual(len(split), 19)
        self.assertEqual(split, EXPECTED_SPLIT)

    def test_splitwaves_do_not_include_invalid(self):
        split = splitwaves(FALSY_HELLO_WORLD, include_invalid=False)
        self.assertEqual(len(split), 13)
        self.assertEqual(split, EXPECTED_SPLIT[: -len(BAD)])
