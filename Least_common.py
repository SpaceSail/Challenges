"""n number is given. N consists of a and b, n = a + b. Task is to find a pair of a and b with a smallest
common multiple """
n = int(input())
c = []
d = []

for b in range(1, n):
    '''find a pair of numbers'''
    a = n - b
    c.append(a)
    d.append(b)


def least_common_multiple(x, y):
    """define smallest common multiple for pair"""
    if x > y:
        g = x
    elif y > x:
        g = y
    elif y == x:
        g = x
        g = y
    while True:
        if (g % x == 0) and (g % y == 0):
            lcm = g
            break
        else:
            g = g + 1
    return lcm


r = list(map(least_common_multiple, c, d))
'''Send pairs of numbers as arguments to function'''

pair = n - min(r)
'''finding pair with minimal smallest common multiple'''

print('\n', c, '\n', d, '\n', pair, min(r))
