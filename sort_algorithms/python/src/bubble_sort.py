__all__ = "bubble_sort", "bubble_sort_optimized"


def bubble_sort(items):
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, len(items)):
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
    return items


def bubble_sort_optimized(items):
    n = len(items)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
        n -= 1
    return items
