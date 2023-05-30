def binary_search(sorted_list, value):
    left = 0
    right = len(sorted_list)-1
    while left <= right:
        mid = (left+right)//2
        if sorted_list[mid] == value:
            return mid
        if sorted_list[mid] > value:
            right = mid-1
        else:
            left = mid+1
    return -1
