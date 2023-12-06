num = int(input("enter a number"))

def recursive(n):
    
    if  n<10:
        return n
    else:
       
        return n % 10 + recursive(n//10)        

result = recursive(num)

print(result)