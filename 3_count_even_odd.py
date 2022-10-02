def count(n, a):
    even = 0
    odd = 0
    for i in range(n):
        if int(a[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    print("The total number of even numbers:",even)
    print("The total number of odd numbers:", odd)

n = int(input("Enter the number:"))
a = input().split()
count(n, a)