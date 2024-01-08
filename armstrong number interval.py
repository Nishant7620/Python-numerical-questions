num = int(input("enter a number"))
l = len(str(num))
temp = 0
sum = 0
check = num
for i in range(1,num):
    while num>0:
        temp = num%10
        sum = sum+temp**int(l)
        num=num//10
    if sum == check:
        print(sum)
        
          
