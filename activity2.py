def cube(num):
    return num*num*num
def three(num):
    if num %3 ==0:
        return cube(num)
    else:
        return False
print(three(5))
print(three(8))