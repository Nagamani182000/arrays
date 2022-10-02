def maximum_ele(n, a):
    maxi = 0
    for i in a:
        if i > maxi:
            maxi = i
    print("The maximum of element:", maxi)
    return maxi

def minimum_ele(n, a, m):
    mini = m
    for i in a:
        if i < mini:
            mini = i
    print("The minimum of element:", mini)
n = int(input("Enter the number:"))
a = []
for i in range(n):
    a.append(int(input()))
m = maximum_ele(n, a)
minimum_ele(n, a, m)