def insertionSort(list):
    length = len(list)
    #go through whole list
    for i in range(1, length):
        #keep track of current element and its position
        currentElement = list[i]
        currentPosition = i
        #while current element is smaller element on the left and its posion is positive
        while list[currentPosition - 1] > currentElement and currentPosition > 0:
            #move element on the left 1 index to the right
            list[currentPosition] = list[currentPosition - 1]
            #update position of current element
            currentPosition -= 1
        #insert current element into right position
        list[currentPosition] = currentElement
    return list

myList = [343,12,45,13,87,45,25,665,5,234,6,23,5]
print(myList)
print(insertionSort(myList))