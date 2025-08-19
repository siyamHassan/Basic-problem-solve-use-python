import math
user = int(input("Entre number:"))
def prime(n):
    store_number=[]
    for a in range(2,n+1):
        is_prime = True
        for x in range(2,int(math.sqrt(a)+1)):
            if a%x==0:
                is_prime = False
                break
        if is_prime:
           store_number.append(a)

    return store_number
ans = prime(user)
print(ans)