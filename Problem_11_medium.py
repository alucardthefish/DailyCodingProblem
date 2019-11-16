
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string 's' and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


def preprocess(query_set):
	dictionary = {}
	for query_string in query_set:
		word_size = len(query_string)
		for i in range(1, word_size):
			initial_letters = query_string[0:i]
			if dictionary.get(initial_letters):
				dictionary[initial_letters].append(query_string)
			else:
				dictionary[initial_letters] = [query_string]
	return dictionary


def autocomplete(s, queries):
	preprocessed_data = preprocess(queries)
	if preprocessed_data.get(s):
		return preprocessed_data.get(s)
	else:
		return []
