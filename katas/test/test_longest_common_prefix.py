import unittest
from katas.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(longest_common_prefix([]),"")
    
    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["Tameer","Amer"]),"")
    
    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["catdkap","catas","catpasd","cataaa"]),"cat")
    
    def test_mixed_prefix(self):
        self.assertEqual(longest_common_prefix(["catdkap","catas","dograe","doglal"]),"")
    

        
    