
n = int(input('enter a number'))

if n <= 1:
    print("not a prime number")

else :
    if n == 2:
        print("is a prime number")

    else :
        i = 2
        while  n >i:
            if n%i ==0:
                y = 0
                break
                
            else:
                y = 1
            i+=1    

    if y ==0 :
        print("not prime number")

    else :
        print("prime number")  



