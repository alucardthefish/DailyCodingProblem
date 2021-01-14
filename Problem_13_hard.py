"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def getLongestSubstring(s, k):
	longestSubstr = s[0:1]
	sSize = len(s)
	longestSubstrSize = 1;
	for i in range(sSize):
		x = i + 1
		while x < sSize and len(list(dict.fromkeys(s[i:x]))) <= k:
			currentLength = len(s[i:x])
			if currentLength > longestSubstrSize:
				longestSubstr = s[i:x]
				longestSubstrSize = currentLength
			x = x + 1
	return longestSubstr


print(getLongestSubstring("abcba", 2))
print(getLongestSubstring("abcdedev", 2))


