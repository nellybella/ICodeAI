
class Array:
    arr = []

    def __init__(self,arr):
        self.arr = arr
        Array.arr.append(arr)


arr1 = []
arr1.append(Array(2))
print(arr1)

        