from numbers import Number
import sys


class SelectionSort:

    @staticmethod
    def sort(values):
        if not isinstance(values, list):
            raise TypeError("Only a list can be sorted")

        if not all(isinstance(val, Number) for val in values):
            raise ValueError("All list values must be numeric : {}".format(values))

        for i in range(len(values) - 1):
            min_idx = i
            for j in range(i + 1, len(values)):
                if values[j] < values[min_idx]:
                    min_idx = j

            if min_idx != i:
                tmp = values[i]
                values[i] = values[min_idx]
                values[min_idx] = tmp

        return values


if __name__ == "__main__":
    try:
        SelectionSort.sort("Bob")
    except TypeError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    try:
        SelectionSort.sort([1, 15.3, -17, 0, 0.00065])
        SelectionSort.sort([1, 15.3, "Bob"])
    except ValueError:
        type, value, traceback = sys.exc_info()
        print("{} : {}".format(type.__name__, value))

    values = []
    print("Selection sort of {} = {}".format(values, SelectionSort.sort(values.copy())))

    values = [3]
    print("Selection sort of {} = {}".format(values, SelectionSort.sort(values.copy())))

    values = [2, 6, 3, 1, 5, 4]
    print("Selection sort of {} = {}".format(values, SelectionSort.sort(values.copy())))

    values = [201, 26, 3, 0.01, 0.55, 4.456]
    print("Selection sort of {} = {}".format(values, SelectionSort.sort(values.copy())))