
def binary_search(key, sortedList):
    low = 0
    high = len(sortedList) - 1

    while low <= high:
        mid = int((low + high) / 2)
        mid_value = sortedList[mid]

        if mid_value == key:
            return mid
        elif mid_value < key:
            low = mid + 1
        else:
            high = mid -1
    
    return -1


def main():
    unsortedList = [34,32,34,234,23,42,43,234,234,2,423,41,3,12,123,13,13,12,3,423,42,4]
    sortedList = sorted(unsortedList)
    print(sortedList)
    print(binary_search(23,sortedList))

    
# Test function
def test_binary_search():
    testList = [2, 3, 3, 4, 10, 12, 13, 16]
    assert binary_search(12,testList) == 5
    assert binary_search(35,testList) == -1

    

if __name__ == "__main__":
    main()
    test_binary_search()
