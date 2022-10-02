def maximum(n, a):
    maxi = 0
    for i in range(n):
        if a[i] > maxi:
            maxi = a[i]
        return maxi

def count_all(n, a, maxi):
    k = maxi+1
    for i in range(n):
        if a[i] != k:
            count = 1
            for j in range(i+1, n):
                if a[i] == a[j]:
                    count += 1
                    a[j] = k
            print(a[i],"-", count)

n = int(input("Enter the number:"))
a = []
for i in range(n):
    a.append(int(input()))
maxi = maximum(n, a)
count_all(n, a, maxi)