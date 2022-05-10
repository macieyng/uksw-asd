def simple_sort(*args):
    items = list(*args)
    n = len(items)
    for i in range(0, n-1):
        minimal = i
        for j in range(i + 1, n):
            if items[j] < items[minimal]:
                minimal = j
        items[i], items[minimal] = items[minimal], items[i]
    return items



def insert_sort(*args):
    items = list(*args)
    n = len(items)
    for i in range(0, n):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j = j -1
        items[j + 1] = key 
    return items


def bubble_sort(*args):
    items = list(*args)
    n = len (items)
    for i in range(n):
        for j in range(n-1, i, -1):
            if items[j - 1] > items[j]:
                items[j-1], items[j] = items[j], items[j-1]
    return items


def quick_sort(*args):
    items = list(*args)
    n = len(items)
    if n < 2:
        return items
    pivot_index = 0
    pivot_value = items[pivot_index]
    for i in range(pivot_index + 1, n):
        if items[i] <= pivot_value:
            pivot_index = pivot_index + 1
            items[pivot_index], items[i] = items[i], items[pivot_index]
            print(items, pivot_index)
    items[0], items[pivot_index] = items[pivot_index], items[0]
    return quick_sort(items[:pivot_index+1]) + quick_sort(items[pivot_index+1:])


def merge_sort(*args):
    items = list(*args)
    n = len(items)
    if n < 2:
        return items
    if n == 2:
        if items[0] > items[-1]:
            items[0], items[-1] = items[-1], items[0]
            return items
        else:
            return items
    pivot = int(n / 2)
    left = merge_sort(items[:pivot])
    right = merge_sort(items[pivot:])
    left_idx, right_idx = 0, 0
    sorted_items = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_items.append(left[left_idx])
            left_idx += 1
        else:
            sorted_items.append(right[right_idx])
            right_idx += 1
    while left_idx < len(left):
        sorted_items.append(left[left_idx])
        left_idx += 1
    while right_idx < len(right):
        sorted_items.append(right[right_idx])
        right_idx += 1
    return sorted_items
