num = 5

if num<=1:
    print(num)
else:
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)        