import unittest
import Test


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = Test.cap_text(text)
        self.assertEqual(result, "Python")

    def test_mult_words(self):
        text = "monty python"
        result = Test.cap_text(text)
        self.assertEqual(result, "Monty Python")


if __name__ == "__main__":
    unittest.main()
