def bubble_sort(list):
    print(list)
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(list)

bubble_sort([2,1,0,5,6])