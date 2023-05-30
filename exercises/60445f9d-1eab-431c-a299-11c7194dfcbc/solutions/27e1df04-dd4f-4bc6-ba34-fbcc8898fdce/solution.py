def is_consecutive(lst):
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst)-1):
        if sorted_lst[i+1] != sorted_lst[i]+1:
            return False
    return True