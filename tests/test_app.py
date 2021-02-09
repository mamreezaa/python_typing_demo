import app

def test_api():
    mock =  {
        'id'            : 123,
        'name'          : 'mam',
        'age'           : 30,
        'nationality'   : 'Sri Lanka',
    }
    born_in = app.born_in(mock['age'])
    assert born_in == 1990