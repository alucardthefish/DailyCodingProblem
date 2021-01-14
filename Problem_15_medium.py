"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.

"""
import random

def picker(stream):
    
    size = len(stream)
    randFloat = random.uniform(0, size)
    pick = int(randFloat)
    return stream[pick]


print("picker: ", picker([3, 4, 3, 5, 2]))

