"""
Problem 2 (Hard)
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6]
"""


def problem_02(arr_num):
	product = 1
	try:
		for num in arr_num:
			if type(num) is int:
				product *= num
			else:
				raise RuntimeError("List items must be integers only")
		output_list = []
		for num in arr_num:
			output_list.append(product // num)
		return output_list
	except Exception as e:
		print(e)
