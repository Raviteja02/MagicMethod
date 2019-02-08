

def rec_fact(x):
    if x == 1:
        return 1
    else:
        return(x*rec_fact(x-1))
num = int(input("enter a number: "))
if num > 1:
    res = rec_fact(num)
print("factorial of ",num,"is",res)