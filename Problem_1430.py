"""
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i

"""

class SparseArray:
    def __init__(self, arr, size) -> None:
        self.sparse_array = {}
        self.size = size
        if self.size != len(arr):
            raise Exception("There is no match in sizes")
        for index, value in enumerate(arr):
            if value != 0:
                self.sparse_array[index] = value

    def set(self, i, val) -> None:
        if 0 <= i < self.size:
            self.sparse_array[i] = val
        else:
            raise Exception("index out of bound")

    def get(self, i) -> int:
        if self.size > i >= 0:
            return self.sparse_array.get(i, 0)
        else:
            raise Exception("index out of bound")

    def get_data(self) -> dict:
        return self.sparse_array


x_array = [0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 77, 0]
x = SparseArray(x_array, 12)
print("Data: ", x.get_data())
print("Data at index 2: ", x.get(2))
print("Data at index 10: ", x.get(10))

x.set(2, 21)
print("Data: ", x.get_data())