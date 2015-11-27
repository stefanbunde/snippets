__all__ = "selection_sort",


def selection_sort(items):
    n = len(items)

    for j in range(n):
        i_min = j
        for i in range(j+1, n):
            if items[i] < items[i_min]:
                i_min = i
        if not i_min == j:
            items[j], items[i_min] = items[i_min], items[j]
    return items
