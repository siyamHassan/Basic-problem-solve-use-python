'''
1.A single integer n
2.Multiplication table of n from n × 1 to n × 10
'''
n = int(input("Entre a number:"))
# use for loop
for a in range(1,10+1):
    print(f"{n}*{a}={n*a}")
# use while loop
i = 1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i=i+1
