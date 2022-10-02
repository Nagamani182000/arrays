def maximum(n, a):
    maxi = 0
    for i in range(n):
        if a[i] > maxi:
            maxi = a[i]
    return maxi

def count_duplicate(n, a, maxi):
    k = maxi+1
    count = 0
    for i in range(n):
        if a[i] != k:
            for j in range(i+1, n):
                if a[i] == a[j]:
                    count += 1
                    a[j] = k
    print("The count of duplicate:", count)

n = int(input("Enter the number:"))
a = input().split()
for i in range(n):
    a[i] = int(a[i])
maxi = maximum(n, a)
count_duplicate(n, a, maxi)