import unittest
import average

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_average1(self):
        self.assertEqual(average.avg([1,2,3,4,5]), 3)

    def test_average2(self):
        self.assertEqual(average.avg([]), 0)

    def test_average3(self):
        self.assertEqual(average.avg([0,0,0]), 0)

    def test_average4(self):
        self.assertEqual(average.avg("hello"), "Not a valid input")

    def test_average5(self):
        self.assertEqual(average.avg(5), "Not a valid input")

    def test_average6(self):
        self.assertEqual(average.avg([1,2,'g',4,5]), "Not a valid input")

    def test_average7(self):
        self.assertEqual(average.avg([1,2,"hi",4,5]), "Not a valid input")


if __name__ == "__main__":
    unittest.main()
