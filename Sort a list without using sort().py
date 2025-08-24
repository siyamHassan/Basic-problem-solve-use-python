import string
low = string.ascii_lowercase
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
new = []
for a in low:
    for b in thislist:
        if b.startswith(a):
            new.append(b)
print(new)
# output:['banana', 'kiwi', 'mango', 'orange', 'pineapple']
