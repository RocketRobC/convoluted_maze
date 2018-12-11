from random import randrange, shuffle

class QuickSort(object):
    def __init__(self, sort_list, start, end):
        self.list = sort_list
        self.start = start
        self.end = end

    def sort(self):
        if self.start >= self.end:
            return
        pivot_idx = randrange(self.start, self.end + 1)
        pivot_val = self.list[pivot_idx]
        self.swap_vals(pivot_idx, self.end)
        lesser_pointer = self.start
        
        for i in range(self.start, self.end):
            if self.list[i] < pivot_val:
                self.swap_vals(i, lesser_pointer)
                lesser_pointer += 1

        self.swap_vals(self.end, lesser_pointer)
        QuickSort(self.list, self.start, lesser_pointer - 1).sort()
        QuickSort(self.list, lesser_pointer + 1, self.end).sort()
        return self.list

    def swap_vals(self, idx1, idx2):
        self.list[idx2], self.list[idx1] = self.list[idx1], self.list[idx2]


class MergeSort(object):
    def sort(self, items):
        if len(items) <= 1:
             return items
        mid_idx = len(items) // 2
        left_split = items[:mid_idx]
        right_split = items[mid_idx:]
        left_sorted = self.sort(left_split)
        right_sorted = self.sort(right_split)
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        result = []
        while (left and right):
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        if left:
            result += left
        if right:
            result += right

        return result
