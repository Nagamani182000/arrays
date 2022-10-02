def maximum(n, a):
    maxi = 0
    for i in range(n):
        if a[i] > maxi:
            maxi = a[i]
    return maxi

def qnique_number(n, a, maxi):
    k = maxi + 1
    for i in range(n):
        if a[i] != k:
            f = 1
            for j in range(i+1, n):
                    if a[i] == a[j]:
                        f = 0
                        a[j] = k
            if f == 1:
                print(a[i], end=" ")
     
n = int(input("Enter the number:"))
a = input().split()
for i in range(n):
    a[i] = int(a[i])
maxi = maximum(n, a)
qnique_number(n, a, maxi)