num = int(input("enter a number"))
sum = 0
if num<10:
    print("enter valid number")
else:
    for i in str(num):
        sum =sum+int(i)
    print(sum)