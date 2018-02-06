#this sub finds the index for the given num by finding the midpoint, seeing if it's higher or lower and reapeats until it find the mun.
def binarySearch(aList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(aList)-1
    #while loop to check if the num is found or not
    while first <= last and found == False:
        #finds the midpoint
        midpoint = int((int(first) + int(last))/2)
        if aList[midpoint] == itemSought:
            #ends while loop if midpoint is num
            found = True
            index = int(midpoint)
        else:
            #decreases search area based on if num is higher or lower than midpoint
            if aList[midpoint] < itemSought:
                first = int(midpoint) + 1
            else:
                last = int(midpoint) - 1
    return index

#list of numbers in order
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#main program
print (binarySearch(nums, 12))
