
'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def problem_07(encoded_msg):
	size = len(encoded_msg)
	counter = 1

	for index in range(size - 1):
		two_digit_code = int(encoded_msg[index:index+2])
		if 9 < two_digit_code <= 26:
			counter += 1
			idx = index + 2
			for i in range(idx, size - 1):
				tdc = int(encoded_msg[i:i+2])
				if 9 < tdc <= 26:
					counter += 1
	return counter
