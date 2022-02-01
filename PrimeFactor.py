
from math import remainder


def PrimeFactor(num):
    res = []
    if num == None or num <= 0:
        raise Exception("Sorry, None and numbers equal to or below zero are not valid") 
    remainder = int(num)
    if 1 == remainder:
        return res
    divisor = 2
    while remainder > 1:
        while remainder > 0 and remainder % divisor == 0:
            res.append(divisor)
            remainder = remainder/divisor
        divisor+=1
    return res