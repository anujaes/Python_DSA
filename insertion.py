
def insertion (arr):
    list = arr[:]

    for i in range(1, len(list)):
        j = i-1
        key = list[i]
        while j>=0 and list[j]>key :
            list[j+1] = list[j]
            j = j-1

        list[j+1] = key

    return list

unsorted = [12,2,3,55,3,90,1,34]
sorted   = insertion(unsorted)

print('unsorted > ',unsorted)
print('sorted   > ',insertion(unsorted))
