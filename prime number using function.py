num = int(input("enter a number"))

def prime(n):
    if n<=1:
        print("not prime")
    else:
        if n==2:
            print("prime") 

        else:
            i=2
            while n>i:
                if n%i==0:
                    y=1
                    break
                else:
                    y=0
                i +=1
        if y ==1:
            print("not prime")
        else:
            print("prime")
prime(num)                           

                  