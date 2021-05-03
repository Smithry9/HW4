#cubeVolume.py
#Ryan Smith
#smithry9@oregonstate.edu

def volume(length, width, height):
    if(isValid(length) and isValid(width) and isValid(height)):
        vol = length * width * height
        return vol
    else:
        return "Not a valid input"

def isValid(value):
    if((type(value) is int) or (type(value) is float)):
        if(value >= 0):
            return True
        else:
            return False
    else:
        return False
