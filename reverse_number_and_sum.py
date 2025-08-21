'''
1.take two input
2.reverse the number
3.and sum
'''
# first way to solve this problem
input1 = input("Entre first number:")
input2 = input("Entre second number")
def main(x):
    counter = []
    length = len(x) - 1
    for a in range(length, -1, -1):
        counter.append(int(x[a]))
    return counter
a1 = main(input1)
result1 = int("".join(map(str,a1)))
a2 = main(input2)
result2 = int("".join(map(str,a2)))
print(result1+result2)
#second way to solve
r1 = int(input1[::-1])
r2 = int(input2[::-1])
print(r1+r2)


