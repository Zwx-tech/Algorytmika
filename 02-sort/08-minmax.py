def findMinMax(array):
    if not array:
        return

    minElement = array[0]
    maxElement = array[0]

    for element in array:
        if element < minElement:
            minElemen = element
        if element > maxElement:
            maxElement = element

    return minElemen, maxElement

if __name__ == "__main__":
    print(findMinMax([3, 1, 2, 3, 4, 9, 0, 7, 5, 7, 8]))