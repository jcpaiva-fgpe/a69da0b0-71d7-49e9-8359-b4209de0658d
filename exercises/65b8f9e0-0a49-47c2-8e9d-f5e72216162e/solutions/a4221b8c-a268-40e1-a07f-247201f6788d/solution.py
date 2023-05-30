def find_missing_number(lst):
    n = len(lst)+1
    expected_sum = (n*(n+1))//2
    actual_sum = sum(lst)
    return expected_sum - actual_sum