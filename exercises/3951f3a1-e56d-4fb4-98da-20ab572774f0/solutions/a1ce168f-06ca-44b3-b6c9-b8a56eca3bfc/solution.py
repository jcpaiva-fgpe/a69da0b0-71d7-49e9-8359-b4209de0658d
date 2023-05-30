def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2] + nums[n // 2 - 1]) / 2
    else:
        return nums[n // 2]