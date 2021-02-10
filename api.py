from typing import (
    Dict, Any
)
from models.student import Student


def add(x: int, y: int) -> int:
    """Add two int values

    Args:
        x (int): first int value
        y (int): second int value

    Returns:
        int: addition of x and y
    """
    return x + y


def get_student() -> Dict[str, Any]:
    """get student

    Returns:
        Dict[str, Any]: attributes and value of a student
    """
    student = {
        'id': 1001,
        'name': 'Ahmed',
        'age': 12,
        'nationality': 'Emirati',
    }

    Student(**student)

    return student
