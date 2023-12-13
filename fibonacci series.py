n1 = 0
n2 = 1
n3 = 0
num = int(input("enter a number: "))
print(n1,n2,end = " ")
i =0
while i<=10:
    n3 = n1 + n2

    n1 =n2
    n2 = n3
    i =i+1

    print(n3, end=" ")