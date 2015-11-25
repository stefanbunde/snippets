__all__ = "insertion_sort", "insertion_sort_optimized"


def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items


def insertion_sort_optimized(items):
    for i in range(1, len(items)):
        x = items[i]
        j = i
        while j > 0 and items[j-1] > x:
            items[j] = items[j-1]
            j -= 1
        items[j] = x
    return items
