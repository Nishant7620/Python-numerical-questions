num = int(input("enter a number: "))
l = len(str(num))
temp = 0
sum = 0
check = num
for i in range(1,num):
    
    for j in range (i):
        temp = j%10
        sum =sum + temp**int(l)
        j = j//10
    if check == sum:
        print(j)
    else :
        print(j)
              
