def binary_search(data_list, item):
    low = 0
    high = len(data_list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = data_list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12))