
def myPow(tæller, nævner):
    result = 1
    for index in range(nævner):
        result = result * tæller
    return result


print(myPow(3,2))
