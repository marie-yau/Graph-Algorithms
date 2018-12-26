def bubbleSort(list):
    #how many elements are not sorted yet
    notSorted = len(list)
    swapped = False
    #go through whole list
    for a in range(1, len(list)):
        #goes through unsorted elements
        for i in range(0, notSorted - 1):
            #if element on the right is larger, swap left and rigth elements
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        #update number of unsorted elements
        notSorted -= 1
        #list is sorted when during previous loop, nothing was swapped
        if swapped == False:
            break
    return list

myList = [43,54,15,13,87,545,435,63,245,753,45,2,534,15]
print(myList)
print(bubbleSort(myList))
