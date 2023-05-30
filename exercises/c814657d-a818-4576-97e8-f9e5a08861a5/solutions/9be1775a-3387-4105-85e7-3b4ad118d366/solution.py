def find_highest_and_lowest(numbers):
    numbers = list(map(int,numbers.split()))
    return (max(numbers), min(numbers))