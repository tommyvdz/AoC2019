startinput="402328"
endinput="864247"

def isEqualOrGreater(number):
    digits = list(map(int, str(number)))
    x=0
    while digits[x] <= digits[x+1]:
        x += 1
        if x==5:
            return True
    else:
        return False

def twoSameNumbers(number):
    digits = list(map(int, str(number)))
    x=0
    while x <=5:
        if digits.count(digits[x]) == 2:
            return True
        x+=1
    return False


def isPossible(startinput, endinput):
    possible = 0
    start = int(startinput)
    stop = int(endinput)+1
    for i in range(start,stop):
        if isEqualOrGreater(i) == True:
            if twoSameNumbers(i) == True:
                possible += 1
    return possible

print(isPossible(startinput, endinput))
