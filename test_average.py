import unittest
import average

class testCaseAdd(unittest.TestCase):
    #test cases
    #test with normal list
    def test_average1(self):
        self.assertEqual(average.avg([1,2,3,4,5]), 3)
    #test with decimals (rounds to 2 decimal places)
    def test_average2(self):
        self.assertEqual(average.avg([1.0,2.5,3.6,4.8,5.5]), 3.48)
    #test with empty list
    def test_average3(self):
        self.assertEqual(average.avg([]), 0)
    #test with only zeros
    def test_average4(self):
        self.assertEqual(average.avg([0,0,0]), 0)
    #test with string
    def test_average5(self):
        self.assertEqual(average.avg("hello"), "Not a valid input")
    #test with int not in list
    def test_average6(self):
        self.assertEqual(average.avg(5), "Not a valid input")
    #test with a character
    def test_average7(self):
        self.assertEqual(average.avg([1,2,'g',4,5]), "Not a valid input")
    #test with string in list
    def test_average8(self):
        self.assertEqual(average.avg([1,2,"hi",4,5]), "Not a valid input")


if __name__ == "__main__":
    unittest.main()
