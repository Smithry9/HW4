def fullname(firstName, lastName):
    if(isValid(firstName) and isValid(lastName)):
        return firstName + " " + lastName
    else:
        return "Not a valid input"



def isValid(inputString):
    if(type(inputString) is str):
        if(inputString == ""):
            return False
        else:
            return True
    else:
        return False
