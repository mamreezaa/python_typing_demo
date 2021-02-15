from typing import (
    Dict, Any
)
from models.student import Student


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
