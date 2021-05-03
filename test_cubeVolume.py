import unittest
import cubeVolume

class testCaseAdd(unittest.TestCase):
    #test cases
    def test_volume1(self):
        self.assertEqual(cubeVolume.volume(2,2,2), 8)


if __name__ == "__main__":
    unittest.main()
