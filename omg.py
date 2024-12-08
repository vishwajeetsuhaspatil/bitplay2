def abc(a):
    res= 0
    for i in a:
        res= res^i
    return res
a=[]
n=int(input("enter size"))
while n:
    x=int(input("enter a number"))
    a.append(x)
    n= n-1
print(abc(a))        