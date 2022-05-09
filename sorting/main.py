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
    pass


def merge_sort(*args):
    pass


