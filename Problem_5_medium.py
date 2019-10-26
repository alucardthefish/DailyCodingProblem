'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given the implementation of cons below, implement car and cdr.
'''


def cons(a, b):
	def pair(f):
		return f(a, b)
	return pair


def car(cons_func):
	return cons_func(lambda a, b: a)


def cdr(cons_func):
	return cons_func(lambda a, b: b)
