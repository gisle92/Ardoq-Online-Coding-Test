import unittest
import ardoq_highest


class TestArdoqHighest(unittest.TestCase):

    def test_highest_product(self):

        self.assertEqual(ardoq_highest.highest_product([10,10,10,5,5,1],3),1000)
        self.assertRaises(ValueError,ardoq_highest.highest_product,[10,10,10,5,5,1],"b")
        self.assertRaises(ValueError,ardoq_highest.highest_product,[10,10,10,5,5,"b"],3)
        self.assertRaises(ValueError, ardoq_highest.highest_product, [10, 10, 10, 5, 5, 1], -1)
        self.assertRaises(ValueError,ardoq_highest.highest_product,[10,10,10,5,5,1],10)


if __name__=='__main__':
    unittest.main()