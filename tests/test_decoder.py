import unittest

from oceanscript import OceanScriptError, decode


class DecoderTest(unittest.TestCase):
    def test_traceback_position_accuracy(self):
        try:
            decode("^<.^-.^>.#")
        except OceanScriptError as err:
            self.assertEqual(err.position, 9)

        try:
            decode("Z")
        except OceanScriptError as err:
            self.assertEqual(err.position, 0)

    def test_decoding_stretch_mode(self):
        self.assertEqual(decode("*_-...^<..*^<..._-..\n*~>.^-.*_>.^-..*_<."), "ZjSq FbIkG")
        self.assertEqual(decode("*^-._>..*^>.._-..\n*_-.._<..*~>..~>..*_-.."), "BrLq QpOoQ")
        self.assertEqual(decode("*^>._>..*~>.^-..\n*_<.._-.*^-...~-...*^>."), "CrFk PhTwC")
        self.assertEqual(decode("*~>...~-...*~>..^-...\n*_<...^<...*~>...^>.*~<..."), "XwOt YsXcV")
        self.assertEqual(decode("*^>..._<.*~-..^<..\n*~-.._>..*_<.~>.*^<."), "UgNj NrGfA")
        self.assertEqual(decode("*_<._-..*_-._<..\n*_<.~-..*^<..^<..*~<.."), "GqHp GnJjM")
        self.assertEqual(decode("*^-...~>...*~-..^<...\n*~>.^-.*~>..~-...*^-.."), "TxNs FbOwK")
        self.assertEqual(decode("*_<._<..*~-..^<...\n*^>..~>...*_-...~-...*_<.."), "GpNs LxZwP")
        self.assertEqual(decode("*~-.^>..*~>..^<..\n*^<.._>..*_>._-.*~>..."), "ElOj JrIhX")
        self.assertEqual(decode("*_-..._-...*_<.^-.\n*^>..~>...*~-.._>..*~<."), "ZzGb LxNrD")
        self.assertEqual(decode("*^>..~<.*~-..~-.\n*~<.~<.*^-...^<..*~-.."), "LdNe DdTjN")
        self.assertEqual(decode("*^>._>.*_>.._-..\n*~<...~>...*~>..^<...*^-.."), "CiRq VxOsK")
        self.assertEqual(decode("*~-...~<.*~<...^-..\n*_>.._>..*^>.~>.*^<..."), "WdVk RrCfS")
        self.assertEqual(decode("*_<._<...*^-..._-..\n*^-.~-..*~>..^<...*~-.."), "GyTq BnOsN")
        self.assertEqual(decode("*_<..~<.*~<...~>..\n*_-.^>..*_>..^>..*_<.."), "PdVo HlRlP")
        self.assertEqual(decode("*~<.^<.*^>.~-.\n*^>..~-...*^<.^-.*~-."), "DaCe LwAbE")
        self.assertEqual(decode("*^<.._<.*_-..._>.\n*_<.^-..*_-.~<...*_>.."), "JgZi GkHvR")
        self.assertEqual(decode("*~>..._<.*_<...^<...\n*~>...~>.*_<...^-.*~-."), "XgYs XfYbE")
        self.assertEqual(decode("*_-..._>..*_<...~<.\n*_-._-..*_>.._-...*~>.."), "ZrYd HqRzO")
        self.assertEqual(decode("*^-._>..*^-.~>...\n*~>..^-...*^-._<...*^-.."), "BrBx OtByK")

    def test_decoding_squash_mode(self):
        self.assertEqual(decode("*^>..._-...*^>.^<.*^>.._-.*_-.^>.*_<..."), "UzCaLhHcY")
        self.assertEqual(decode("*^-..~>...*^>...^<...*_>.^-..*~<..._-..*^-."), "KxUsIkVqB")
        self.assertEqual(decode("*^-.^<..*~>._-...*^-..._-...*_-..._-.*_-..."), "BjFzTzZhZ")
        self.assertEqual(decode("*^-..^-...*~>...^>...*~<...^>.*~>..^-.*_>.."), "KtXuVcObR")
        self.assertEqual(decode("*_>..~>...*_-.^-.*^>..._-.*~-..~>.*~-.."), "RxHbUhNfN")
        self.assertEqual(decode("*_<...^<.*_<._-.*~>._>..*_<.._-..*~<..."), "YaGhFrPqV")
        self.assertEqual(decode("*~>.._-.*~<.~<.*_<.._-.*_>.._>.*~>..."), "OhDdPhRiX")
        self.assertEqual(decode("*~<...~>...*^-.~>.*~-.^-...*~>...~<...*~-.."), "VxBfEtXvN")
        self.assertEqual(decode("*~-..~-...*~>..^<.*_<.._>..*^-..._-..*~<..."), "NwOaPrTqV")
        self.assertEqual(decode("*_-.^-.*^>..~-.*_>._-..*~<..^<..*_<.."), "HbLeIqMjP")
        self.assertEqual(decode("*~<...^<.*~-..~-.*^<._-.*~-..^<...*_-.."), "VaNeAhNsQ")
        self.assertEqual(decode("*^>.._>.*~-...~-...*^>.^-..*^>.~<...*~-.."), "LiWwCkCvN")
        self.assertEqual(decode("*^-..^-..*^>..^>...*~-.^>..*~-.._>..*_<..."), "KkLuElNrY")
        self.assertEqual(decode("*^<.^>..*_>..~>.*^<...^<..*~<._<..*^-..."), "AlRfSjDpT")
        self.assertEqual(decode("*~>..^>..*~>..._-..*~<..^-.*~-..~-...*_>."), "OlXqMbNwI")
        self.assertEqual(decode("*~<.._>..*~>._<...*_>._<.*^-.._>..*~>..."), "MrFyIgKrX")
        self.assertEqual(decode("*^>..^-.*^<.^<..*_-.~<.*^<.^<...*~-..."), "LbAjHdAsW")
        self.assertEqual(decode("*^-..._>.*^-.~>...*_<.~>.*^-.._<...*~>.."), "TiBxGfKyO")
        self.assertEqual(decode("*^>..~>...*~>.._<.*^<.~>..*_>.._-..*^>.."), "LxOgAoRqL")
        self.assertEqual(decode("*~<..~<...*^<.~-..*_<.^>.*^-.~<..*_-..."), "MvAnGcBmZ")

    def test_splash_rule_integers(self):
        with self.assertRaises(OceanScriptError):
            decode("*_>...")  # capitalized 0
            decode("*^>....")  # capitalized 3
            decode("*_>....")  # capitalized 9

    def test_splash_rule_capitalized(self):
        with self.assertRaises(OceanScriptError):
            decode("*=Δ")  # capitalized delta
            decode("*=Λ")  # capitalized lambda

    def test_splash_rule_non_alpha(self):
        with self.assertRaises(OceanScriptError):
            decode("*==")
            decode("*=.")
            decode("*=?")
