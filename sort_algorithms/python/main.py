import random
import timeit

from src import bubble_sort, bubble_sort_optimized, insertion_sort, insertion_sort_optimized


short_list = list(range(10))
long_list = list(range(10000))

random.shuffle(short_list)
random.shuffle(long_list)


def main():
    for sort_method in ["bubble_sort", "bubble_sort_optimized", "insertion_sort",
                        "insertion_sort_optimized"]:
        duration = timeit.timeit(stmt="{}(short_list[:])".format(sort_method),
                                 setup="from __main__ import {}, short_list".format(sort_method),
                                 number=100000)
        print("{} 100.000 times with 10 items: {}".format(sort_method, duration))

        duration = timeit.timeit(stmt="{}(long_list[:])".format(sort_method),
                                 setup="from __main__ import {}, long_list".format(sort_method),
                                 number=1)
        print("{} 1 time with 10000 items: {}".format(sort_method, duration))


if __name__ == "__main__":
    main()
