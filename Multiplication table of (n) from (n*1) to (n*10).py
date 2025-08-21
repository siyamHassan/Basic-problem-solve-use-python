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
# output:
# 13*1=13
# 13*2=26
# 13*3=39
# 13*4=52
# 13*5=65
# 13*6=78
# 13*7=91
# 13*8=104
# 13*9=117
# 13*10=130
