def mergeSort(list):
    length = len(list)

    if length <= 1:
        return list
    else:
        middleIndex = int(length / 2)
        #divide list into left and right list
        leftList = list[0:middleIndex]
        rightList = list[middleIndex:]
        #recursive calls
        mergeSort(leftList)
        mergeSort(rightList)

        #list indexes
        i = j = k = 0
        #merge and sort left and right lists until one reaches the end
        while len(leftList) > i and len(rightList) > j:
            if leftList[i] < rightList[j]:
                list[k] = leftList[i]
                i += 1
            else:
                list[k] = rightList[j]
                j += 1
            k += 1
        #if any element left in left list, append it to the list
        while i < len(leftList):
            list[k] = leftList[i]
            i += 1
            k += 1
        #if any element left in right list, append it to the list
        while j < len(rightList):
            list[k] = rightList[j]
            j += 1
            k += 1
        return list

myList = [67,34,3,56,24,77,23,89,56,35,65,764]
print("List\n", myList)
print("Sorted List\n", mergeSort(myList))