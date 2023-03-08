"""n is given. Task is to print quantity of simple numbers wich is strictly less then n """
n = int(input())
count = 0
a = list(i for i in range(2,n))
for k in a:
    if k < n:
        count += 1
    else:
        pass
print(a)
print(count)