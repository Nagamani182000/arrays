def count(n, a):
    poi = " "
    neg = []
    for i in range(n):
        if int(a[i]) > 0:
            poi += a[i]
        else:
            neg.append(a[i])
    print(poi)
    print(neg)
n = int(input("Enter the number:"))
a = input().split()
count(n, a)