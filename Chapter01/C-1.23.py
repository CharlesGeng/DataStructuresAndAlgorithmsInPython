# Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

data = list(range(10))

try:
    data[12] = 100
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
