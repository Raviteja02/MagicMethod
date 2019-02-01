x = [1,20,30,40,50,60]
print(len(x))

p = 0
while True:
    i = int(input("enter element to search :"))
    if i in x:

        print(i,"guess number found")
        break
    else:
        p=p+1
        if p == 3:
            print("you have exceeded maximum number of trails")
            break
        print("search element not found")
