u = input("Entre number:")#here take input
# first way
new = []
for a in u:
    new.append(int(a))
print(max(new),"is big")
# another way
alternative = [int(a) for a in u]
print(max(alternative),' is big')