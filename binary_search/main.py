def binary_search(*args, key):
    """-1 means not found"""
    items = list(args)
    n = len(items)
    if n == 1 and key != items[0]:
        return -1
    mid = int(n / 2)
    if key == items[mid]:
        return mid
    if key < items[mid]:
        return binary_search(*items[:mid], key=key)
    result = binary_search(*items[mid:], key=key)
    return result + mid if result >= 0 else result
