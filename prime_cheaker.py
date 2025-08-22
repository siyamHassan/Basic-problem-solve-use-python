u = int(input("Entre a number:"))
if u<=1:
    print(u,'is not prime')
else:
    is_prime=True
    for a in range(2,u):
        if u%a==0:
            is_prime= False
            break
    if is_prime:
        print(u,"is prime")
    else:
        print(u,'is not prime')
