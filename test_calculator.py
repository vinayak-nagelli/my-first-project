from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5 , "here add test failed "

def test_subtract():
    assert subtract(5, 3) == 2 , "here subtract test failed "

def test_multiply():
    assert multiply(4, 3) == 12  , "here multiply test failed "

def test_divide():
    assert divide(10, 2) == 5  , "here divide test failed "