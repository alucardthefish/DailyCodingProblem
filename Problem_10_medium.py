import time

# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


def job_scheduler(f, n):
	start = time.time_ns() // 1000000
	while True:
		end = time.time_ns() // 1000000
		if end - start > n:
			f()
			break


def hello_world():
	print("Hello World!")


def test():
	start = time.time_ns() // 1000000
	job_scheduler(hello_world, 3000)
	end = time.time_ns() // 1000000
	duration = end - start
	print("The function was called after:", duration, "milliseconds")
