
# This problem was asked by Amazon.
#
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
# that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
# integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def climb(N, X):
	# Initialize memory for dynamic programming
	size = N + 1
	memory = [0 for i in range(size)]
	memory[0] = 1
	for i in range(size):
		memory[i] += sum(memory[i-x] for x in X if i-x > 0)
		memory[i] += 1 if i in X else 0
	return memory[-1]