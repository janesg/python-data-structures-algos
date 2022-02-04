# Time complexity : O(n log n)
#   - sort      : recursively reducing size of list to sort : O(log n)
#   - pivot     : loop through each element : O(n)

# Note: Time complexity is O(n2) if we have already sorted data
# Space complexity : O(n)

class QuickSort:

    @staticmethod
    def sort(input):
        return QuickSort.__qs_helper(input, 0, len(input) - 1)

    # Private static method
    @staticmethod
    def __qs_helper(input, left_idx, right_idx):
        if left_idx < right_idx:
            pvt_idx = QuickSort._pivot(input, left_idx, right_idx)
            QuickSort.__qs_helper(input, left_idx, pvt_idx - 1)
            QuickSort.__qs_helper(input, pvt_idx + 1, right_idx)

        return input

    # Protected static method - so we can call it from __main__ below
    @staticmethod
    def _pivot(input, pvt_idx, end_idx):
        swap_idx = pvt_idx

        for i in range(pvt_idx + 1, end_idx + 1):
            if input[i] < input[pvt_idx]:
                swap_idx += 1
                QuickSort.__swap(input, i, swap_idx)

        QuickSort.__swap(input, pvt_idx, swap_idx)

        return swap_idx

    # Private static method
    @staticmethod
    def __swap(input, idx_1, idx_2):
        tmp = input[idx_1]
        input[idx_1] = input[idx_2]
        input[idx_2] = tmp


if __name__ == "__main__":

    my_list = [4, 6, 1, 7, 3, 2, 5]
    start_list = my_list.copy()
    pvt_idx = QuickSort._pivot(my_list, 0, len(my_list) - 1)
    print("Pivot of {} = {} with pivot idx of {}".format(start_list, my_list, pvt_idx))

    my_list = []
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))

    my_list = [6]
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))

    my_list = [6, 1]
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))

    my_list = [4, 6, 1, 7, 3, 2, 5]
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))

    my_list = [12, 11, 10, 9, 8, 7, 6, 4, 5, 3, 2, 1]
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))

    # With duplicates
    my_list = [12, 11, 10, 9, 8, 7, 6, 4, 5, 4, 3, 3, 2, 1, 1]
    start_list = my_list.copy()
    QuickSort.sort(my_list)
    print("Quick sort of {} = {}".format(start_list, my_list))