from src import task2

def test_datatypes():
    datatypes = task2.get_datatypes()
    assert type(datatypes["int"]) == int
    assert type(datatypes["float"]) == float
    assert type(datatypes["str"]) == str
    assert type(datatypes["bool"]) == bool

if __name__ == "__main__":
    test_datatypes()