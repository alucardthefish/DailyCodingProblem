# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
# since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# Input examples
input_1 = [2, 4, 6, 2, 5]				# return 13
input_2 = [5, 1, 1, 5]					# return 10
input_3 = [2, 14, 6, 2, 15]				# return 29
input_4 = [2, 5, 11, 8, 3]				# return 16
input_5 = [90, 15, 10, 30, 100]			# return 200
input_6 = [29, 51, 8, 10, 43, 28]		# return 94


def largest_sum_adj(arr):
	result = 0
	size = len(arr)
	# validate the input list. It must be a length greater than 2
	if size > 2:
		arr[2] += arr[0]
		result = arr[2]
		for i in range(3, size):
			tmp = arr[i-3]
			if arr[i-2] > arr[i-3]:
				tmp = arr[i-2]
			tmp_addition = tmp + arr[i]
			arr[i] = tmp_addition
			if tmp_addition > result:
				result = tmp_addition
	else:
		print("The length of input list must be greater than 2")
	return result
