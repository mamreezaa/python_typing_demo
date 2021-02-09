import app

def test_born_in():
    """Test born_in function
    """
    mock =  {
        'id'            : 123,
        'name'          : 'mam',
        'age'           : 30,
        'nationality'   : 'Sri Lanka',
    }
    born_in = app.born_in(mock['age'])
    assert born_in == 1990