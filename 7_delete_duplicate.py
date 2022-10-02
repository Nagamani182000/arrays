import re


def maximum(n, elements):
    maxi = 0
    for i in range(n):
        if elements[i] > maxi:
            maxi = elements[i]
    return maxi
def delete_duplicate(n, elements, maxi):
    k = maxi + 1
    for i in range(n):
        if elements[i] != k:
            print(elements[i], end=" ")
            for j in range(i+1, n):
                if elements[i] == elements[j]:
                    elements[j] = k
        
n = int(input("Enter the number:"))
elements = input().split()
for i in range(n):
    elements[i] = int(elements[i])
maxi = maximum(n, elements)
delete_duplicate(n, elements, maxi)