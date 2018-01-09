def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList)-1
    while first <= last and found == False:
        midpoint = int((int(first) + int(last))/2)
        if aList[midpoint] == itemSought:
            found = True
            index = int(midpoint)
        else:
            if aList[midpoint] < itemSought:
                first = int(midpoint) + 1
            else:
                last = int(midpoint) - 1
    return index

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

print (binarySearch(nums, 12))
