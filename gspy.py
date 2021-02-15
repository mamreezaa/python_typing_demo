from typing import (
    List,
)

def add(x : float, y : float) -> float:
    """add two numbers

    Args:
        x (float): first number
        y (float): 2nd number

    Returns:
        float: addition of x and y
    """
    return x + y

def add_all(nums : List[float]) -> float:
    """Add all numbers in a list

    Args:
        nums (List[float]): List of numbers

    Returns:
        float: addition of all numbers
    """
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum