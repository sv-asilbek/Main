def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element indeksini qaytaradi
    return -1  # Element topilmadi


arr = [5, 2, 9, 1, 7]
target = 9
result = linear_search(arr, target)
if result != -1:
    print("Element", target, "indeksida")
else:
    print("Element topilmadi")


def search(arr1, x):
    for i in range(len(arr1)):

        if arr1[i] == x:
            return i

    return -1
