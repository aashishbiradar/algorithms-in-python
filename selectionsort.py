def selection_sort(list):
    print(list)
    n = len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list[i] > list [j]:
                list[i],list[j] = list[j],list[i]
    print(list)

selection_sort([2,1,0,5,6])

    