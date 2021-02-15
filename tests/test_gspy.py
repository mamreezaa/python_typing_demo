import gspy as gs
import pytest

def test_add_with_int_numbers():
    assert gs.add(2, 4) == 6

def test_add_with_float_numbers():
    assert gs.add(2.4, 4.6) == 7.0

def test_add_for_type_error():
    with pytest.raises(TypeError):
        gs.add(2.4, 'two')