
def swap(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

def Selection(arr):
    list = arr[:]
    length = len(list)
    for i in range( 0,length):
        smallest = i
        for j in range(i+1,length):
            if list[j] < list[smallest]:
                smallest = j
        swap(list,i,smallest)

    return list

unsorted = [12,4,122,6,4,78,0,2,4]
sorted = Selection(unsorted)

print('unsorted > ',unsorted)
print('sorted   > ',sorted)
