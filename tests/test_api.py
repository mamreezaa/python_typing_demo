import api


def test_api_add():
    """Test add function
    """
    total = api.add(2, 3)
    assert total == 5


def test_api_get_student():
    """Test get student function
    """
    student = api.get_student()
    assert type(student) == dict
