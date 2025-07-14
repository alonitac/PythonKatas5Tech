import unittest
from katas.matrix_rotate import rotate_matrix


class TestRotateMatrix(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(rotate_matrix([[]]),[[]])
    
    def test_not_square_matrix(self):
        self.assertEqual(rotate_matrix([[1,2,3],[1,2,1]]),"Matirx is not square")
    
    def test_rotation(self):
        self.assertEqual(rotate_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]),[[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    

        
    