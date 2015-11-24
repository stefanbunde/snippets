def bubble_sort(items):
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, len(items)):
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
    return items
