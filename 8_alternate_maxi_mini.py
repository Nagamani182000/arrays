def maximum_element(n, a):
    maxi = 0
    for i in range(n):
        if a[i] > maxi:
            maxi = a[i]
    return maxi

def maximum(n, a, k):
    maxi = 0
    for i in range(n):
        if a[i] != k:
            if a[i] > maxi:
                maxi = a[i]
                position = i
    a[position] = k
    print(maxi, end=" ")

def minimum(n, a, k):
    mini = k
    for i in range(n):
        if a[i] != k:
            if a[i] < mini:
                mini = a[i]
                position = i
    a[position] = k
    print(mini, end=" ")

n = int(input("Enter the number:"))
a = input().split()
for i in range(n):
    a[i] = int(a[i])
maxi = maximum_element(n, a)
k = maxi + 1
tot = n // 2

while tot > 0:
    maximum(n, a, k)
    minimum(n, a, k)
    tot -= 1
if n % 2 != 0:
    maximum(n, a, k)