import unittest
from katas.word_count import count_words


class TestWordCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)
    
    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)
    
    def test_multiple_words(self):
        self.assertEqual(count_words("This is a test"), 4)
    
    def test_leading_trailing_spaces(self):
        self.assertEqual(count_words("   Leading         a  "), 2)

    


