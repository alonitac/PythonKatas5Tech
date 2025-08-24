import unittest
from katas.word_count import count_words
class TestCountWords(unittest.TestCase):

    def test_regular_sentence(self):
        self.assertEqual(count_words("This is a test."), 4)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("   Too   many   spaces   "), 3)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_only_spaces(self):
        self.assertEqual(count_words("     "), 0)

    def test_newlines_and_tabs(self):
        self.assertEqual(count_words("Line1\nLine2\tLine3"), 3)

    def test_punctuation(self):
        self.assertEqual(count_words("Hi, there! How are you?"), 5)