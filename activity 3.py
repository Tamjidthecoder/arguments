def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
fat1=int(input("enter a value for fact: "))
print(fact(fat1))
    