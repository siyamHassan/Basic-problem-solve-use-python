user = int(input("Entre a number:"))#here input
#1. use mathmatical logic to solve
def sum_loop(n):
    ans = n*(n+1)//2
    return ans
result = sum_loop(user)
print(result)
#2. use loop and counter variable to solve
counter = 0
for a in range(1,user+1):
    counter+=a
print(counter)