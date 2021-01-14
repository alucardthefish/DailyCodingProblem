"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

import random


NUM_ITERATIONS = 70000

count_in_circle = 0
count_in_square = 0


for i in range(NUM_ITERATIONS):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    abs_value = x**2 + y**2

    if abs_value <= 1:
        count_in_circle += 1
    count_in_square += 1


pi_estimation = 4 * count_in_circle / count_in_square

formatted_str = "{:.3f}".format(pi_estimation)

pi = float(formatted_str)


print("Estimation of PI = ", pi)