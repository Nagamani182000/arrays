def merge_elements_1(n, m, list_1, list_2):
    tot = list_1 + list_2
    # bubble sort
    for j in range(len(tot)):
        for i in range(len(tot)-1):
            if int(tot[i]) > int(tot[i+1]):
                tot[i],tot[i+1] = tot[i+1],tot[i]
    for i in tot:
        print(int(i), end=" ")

def merge_elements_2(n, m,list_1, list_2):
    tot_list = []
    for i in list_1:
        tot_list.append(int(i))
    for i in list_2:
        tot_list.append(int(i))
    # selection sort
    for i in range(len(tot_list)):
        mini = i
        for j in range(i+1, len(tot_list)):
            if tot_list[j] < tot_list[mini]:
                mini = j
        tot_list[i], tot_list[mini] = tot_list[mini], tot_list[i]
    print("\n", tot_list)

n = int(input("Enter the number n:"))
m = int(input("Enter the number m:"))
list_1 = input().split()
list_2 = input().split()
merge_elements_1(n, m, list_1, list_2)
merge_elements_2(n, m, list_1, list_2)