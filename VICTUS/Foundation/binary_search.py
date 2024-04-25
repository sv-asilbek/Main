# # # Python 3 program for recursive binary search.
# # # Modifications needed for the older Python 2 are found in comments.
# #
# # # Returns index of x in arr if present, else -1
# # def binary_search(arr, low, high, x):
# #
# # 	# Check base case
# # 	if high >= low:
# #
# # 		mid = (high + low) // 2
# #
# # 		# If element is present at the middle itself
# # 		if arr[mid] == x:
# # 			return mid
# #
# # 		# If element is smaller than mid, then it can only
# # 		# be present in left subarray
# # 		elif arr[mid] > x:
# # 			return binary_search(arr, low, mid - 1, x)
# #
# # 		# Else the element can only be present in right subarray
# # 		else:
# # 			return binary_search(arr, mid + 1, high, x)
# #
# # 	else:
# # 		# Element is not present in the array
# # 		return -1
# #
# # # Test array
# # arr = [ 2, 3, 4, 10, 40 ]
# # x = 10
# #
# # # Function call
# # result = binary_search(arr, 0, len(arr)-1, x)
# #
# # if result != -1:
# # 	print("Element is present at index", str(result))
# # else:
# # 	print("Element is not present in array")
# #
# #
# # # -------------------------------------------------------
# # # 35, 704, 2037
#
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element indeksini qaytaradi
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element topilmadi

arr = [1, 2, 5, 7, 9]
target = int(input())
result = binary_search(arr, target)
if result != -1:
    print("Element", target, "indeksida")
else:
    print("Element topilmadi")
#


# d = ['salom', 'hayr', 'hello', 'python']
# for i, j in enumerate(d):
# 	print(i, j)


