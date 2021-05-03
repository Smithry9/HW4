import unittest
import cubeVolume

class testCaseAdd(unittest.TestCase):
    #test cases
    #cube with lenght, width, and height = 2
    def test_volume1(self):
        self.assertEqual(cubeVolume.volume(2,2,2), 8)

    #cube with length = 1.5, width = 2, height = 2.5
    def test_volume2(self):
        self.assertEqual(cubeVolume.volume(1.5,2,2.5), 7.5)

    #cube with length = 0 (makes the volume 0)
    def test_volume3(self):
        self.assertEqual(cubeVolume.volume(0,2,2), 0)

    #invalid result with negative number
    def test_volume4(self):
        self.assertEqual(cubeVolume.volume(2,-1,2), "Not a valid input")

    #invalid result with character
    def test_volume5(self):
        self.assertEqual(cubeVolume.volume(2,'f',2), "Not a valid input")

    #invalid result with string
    def test_volume6(self):
        self.assertEqual(cubeVolume.volume("hello",2,2), "Not a valid input")


if __name__ == "__main__":
    unittest.main()
