num = int(input("enter a number"))

def factorial (n):
    fact = 1
    while n>=1:
        fact =fact*n
        n =n-1
    print(fact)
factorial(num)        