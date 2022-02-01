# Time complexity : O(n log n)
#   - sort      : recursively splitting in half : O(log n)
#   - merging   : combining the single element lists : O(n)
# Space complexity : O(n)
class MergeSort:

    @staticmethod
    def sort(list):
        if len(list) <= 1:
            return list
        else:
            mid_idx = int(len(list) / 2)
            left = list[:mid_idx]
            right = list[mid_idx:]
            return MergeSort.merge(MergeSort.sort(left), MergeSort.sort(right))

    @staticmethod
    # Condition : both lists must be already sorted from lowest value to highest value
    def merge(list_1, list_2):
        len_1 = len(list_1)
        len_2 = len(list_2)

        if len_1 == 0:
            return list_2

        if len_2 == 0:
            return list_1

        output = []
        idx_1 = 0
        idx_2 = 0

        while idx_1 < len_1 and idx_2 < len_2:
            if list_1[idx_1] < list_2[idx_2]:
                output.append(list_1[idx_1])
                idx_1 += 1
            else:
                output.append(list_2[idx_2])
                idx_2 += 1

        while idx_1 < len_1:
            output.append(list_1[idx_1])
            idx_1 += 1

        while idx_2 < len_2:
            output.append(list_2[idx_2])
            idx_2 += 1

        return output


if __name__ == "__main__":

    print(MergeSort.merge([1, 6, 7], [3, 4, 5]))
    print(MergeSort.merge([2], [1, 3, 4, 5]))
    print(MergeSort.merge([], [1, 2, 3, 4, 5]))

    values = []
    print("Merge sort of {} = {}".format(values, MergeSort.sort(values.copy())))

    values = [3]
    print("Merge sort of {} = {}".format(values, MergeSort.sort(values.copy())))

    values = [2, 6, 3, 1, 5, 4]
    print("Merge sort of {} = {}".format(values, MergeSort.sort(values.copy())))

    values = [201, 26, 3, 0.01, 0.55, 4.456]
    print("Merge sort of {} = {}".format(values, MergeSort.sort(values.copy())))
