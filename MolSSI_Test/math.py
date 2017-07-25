"""
A small set of functions for doing math operations.
"""


# Write a function named add that adds two values

def add(A, B):
    """
    Function to add two values A and B, use as "add(A, B)"
    """
    return A + B


def mult(A, B):
    """
    Function to multiply two values A and B, use as "mult(A, B)"
    """
    return A * B


def div(A, B):
    """
    Function to divide two values A and B (A / B), use as "div(A, B)"
    """
    if (B == 0):
        raise Exception("Don't divide by zero!")
    return A / B
