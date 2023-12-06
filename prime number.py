n = int(input('enter a number'))

if n <= 1:
    print("not a prime number")

else :
    if n == 2:
        print("is a prime number")

    else :
        if n%2 ==0:
            y = 0
        else:
            y = 1

        if y ==0 :
                print("not a prime number")

        else :
            print(" prime number")  