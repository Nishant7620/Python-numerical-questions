num = int(input("enter a number: "))
l = len(str(num))
temp = 0
sum = 0
if num<=10:
    print(num)

else:
    while num>0:
        temp = num%10
        sum =sum + temp**int(l)
        num = num//10
    print(sum)    
