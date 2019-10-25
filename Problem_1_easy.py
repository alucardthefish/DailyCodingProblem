"""
Problem 1 (Easy)
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def problem_01(number_list, k):
	i = 1
	flag = False
	for n in number_list[:-1]:
		for m in number_list[i:]:
			if (n + m) == k:
				flag = True
				break
		i = i + 1
	return flag


def problem_01_bonus(num_list, k):
	memory = dict()
	for number in num_list:
		if number <= k:
			expected_pair = k - number
			memo = memory.get(expected_pair)
			if memo:
				return True
			memory[number] = expected_pair
	return False
