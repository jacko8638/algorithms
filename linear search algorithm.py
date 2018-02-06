#goes through list num by num to find the given num
def linearSearch(numlist, numSought):
    index = -1
    i = 0
    found = False
    while i < len(numlist) and found == False:
        if numlist[i] == numSought:
            index = i
            found = True
        i = i + 1
    return index

#test list
numlist = [1,2,3,4,5,6,7,8,9,10,12,14,15,16,25,26,467]

#main program
print(linearSearch(numlist, 16))
