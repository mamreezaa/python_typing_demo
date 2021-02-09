from pydantic import BaseModel

class Student(BaseModel):
    """Create student model

    Args:
        BaseModel (BaseModel): Base model given by pydantic
    """
    id: int
    name: str
    age: int
    nationality: str
