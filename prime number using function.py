num = int(input("enter a number"))

def prime(n):
    if n<=1:
        print("not prime")
    else:
        if n==2:
            print("prime") 

        else:
            if n%2==0:
                y=1
            else:
                y=0

            if y ==1:
                print("not prime")
            else:
                print("prime")
prime(num)                           

                  