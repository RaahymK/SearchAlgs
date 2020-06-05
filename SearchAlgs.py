def linear_search(search_list, target):
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
    return -1



def binary_search(search_list, target):
    start = 0
    end = len(search_list)
    while start < end:
        mid = (end + start) // 2
        if search_list[mid] == target:
            return mid
        elif search_list[mid] < target:
            start = mid + 1
        elif search_list[mid] > target:
            end = mid
    return -1


# Testing done

arr = [1, 10, 11, 40, 69]
arr2 = [1, 2, 3, 55, 1000, 5000000]






