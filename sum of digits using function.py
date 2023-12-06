num1 = int(input("enter a number"))

def sum_of_num (n):
    sum1 = 0
    while  n>0:
        temp = n%10
        sum1= sum1+temp
        n = n//10
    return sum1
        
result = sum_of_num(num1)

print(result)


