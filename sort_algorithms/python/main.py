import random
import timeit

from src import bubble_sort, bubble_sort_optimized, insertion_sort, insertion_sort_optimized


short_list = list(range(10))
long_list = list(range(10000))

random.shuffle(short_list)
random.shuffle(long_list)


class Table(object):
    column_width = 30

    def __init__(self):
        self._rows = []
        self._create_header()

    def _create_header(self):
        self.add_row(" ", "1 list with 10k elements", "100k lists with 10 elements")
        self.add_line()

    def add_line(self):
        self._rows.append("{0}-+-{0}-+-{0}-".format(self.column_width*"-"))

    def add_row(self, column1, column2, column3):
        self._rows.append("{:{width}} | {:>{width}} | {:>{width}}"
                          .format(column1, column2, column3, width=self.column_width))

    def __str__(self):
        return "\n".join(self._rows)


def main():
    table = Table()
    for sort_method in ["bubble_sort", "bubble_sort_optimized", "insertion_sort",
                        "insertion_sort_optimized"]:
        duration1 = timeit.timeit(stmt="{}(long_list[:])".format(sort_method),
                                  setup="from __main__ import {}, long_list".format(sort_method),
                                  number=1)
        duration2 = timeit.timeit(stmt="{}(short_list[:])".format(sort_method),
                                  setup="from __main__ import {}, short_list".format(sort_method),
                                  number=100000)
        table.add_row(sort_method, "{:.4f}".format(duration1), "{:.4f}".format(duration2))
    print(table)


if __name__ == "__main__":
    main()
