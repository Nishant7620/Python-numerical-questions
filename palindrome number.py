num =int(input("enter a number: "))
temp = ""
if num<10:
    print(num)
else:

    for i in str(num):
        temp = i+temp
    if int(temp) ==num:
        print("true")
    else:
        print("false")        