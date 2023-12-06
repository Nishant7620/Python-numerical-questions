prime = lambda num : "not prime" if num<=1  else "prime" if num ==2 else ("not prime" if num%2==0  else "prime ")

print(prime(5))