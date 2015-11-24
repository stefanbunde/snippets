import random
import timeit

from src import bubble_sort


short_list = list(range(10))
long_list = list(range(10000))

random.shuffle(short_list)
random.shuffle(long_list)


def main():
    duration = timeit.timeit(stmt="bubble_sort(short_list[:])",
                             setup="from __main__ import bubble_sort, short_list",
                             number=100000)
    print("bubble sort 100.000 times with 10 items: {}".format(duration))

    duration = timeit.timeit(stmt="bubble_sort(long_list[:])",
                             setup="from __main__ import bubble_sort, long_list",
                             number=1)
    print("bubble sort 1 time with 10000 items: {}".format(duration))


if __name__ == "__main__":
    main()
