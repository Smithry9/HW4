import unittest
import fullName

class testCaseAdd(unittest.TestCase):

    #test with normal first and last name
    def test_fullname1(self):
        self.assertEqual(fullName.fullname("Ryan","Smith"), "Ryan Smith")

    #test with input other than string
    def test_fullname2(self):
        self.assertEqual(fullName.fullname("Ryan", 5), "Not a valid input")

    #test with empty string (should be invalid)
    def test_fullname3(self):
        self.assertEqual(fullName.fullname("","Smith"), "Not a valid input")


if __name__ == "__main__":
    unittest.main()
