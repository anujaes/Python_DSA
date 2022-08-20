def exchange(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def Bubble(list):
    n = len(list)-1
    for i in range(0,n):
        for j in range(n,i,-1):
            if list[j] < list[j-1]:
                list = exchange(list, j, j-1)

    return list

unsorted = [1,4,2,9,0,3,4,6]

print('sorted > ', Bubble(unsorted))
