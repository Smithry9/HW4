def avg(inputList):
    if(len(inputList) <= 0):
        return 0
    total = 0
    for i in inputList:
        if(isValid(i)):
            total += i
        else:
            return "Not a valid input"

    average = total / len(inputList)
    return average

def isValid(value):
    if((type(value) is int) or (type(value) is float)):
        if(value >= 0):
            return True
        else:
            return False
    else:
        return False
