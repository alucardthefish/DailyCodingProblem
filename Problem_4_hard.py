"""
Problem 4 (Hard)
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def problem_04(arr):
	index = 1
	minIndex = 1
	for element in arr:
		if 0 < element <= len(arr):
			var1 = arr[element - 1]
			arr[element - 1] = element
			if 0 < var1 <= len(arr):
				arr[index - 1] = arr[var1 - 1]
				arr[var1 - 1] = var1
			else:
				arr[index - 1] = var1
				if minIndex == arr[minIndex - 1]:
					minIndex = index
				else:
					if minIndex > index:
						minIndex = index
		index = index + 1
	for i in range(1, len(arr)+1):
		if i != arr[i-1]:
			return i
	return len(arr) + 1
