def test_one():
    expeceted_result = 5
    actual_result = 51
    assert actual_result == expeceted_result


def test_two():
    expeceted_result = 5
    actual_result = 5
    assert actual_result == expeceted_result


def test_three():
    assert 1 == 1
    assert 2 == 2
    assert 3 > 2
    assert 4 < 3
    assert 5 >= 5
    assert 6 <= 6
    assert 7 in [1, 2, 3, 4, 5, 6, 7]
    assert 8 not in [1, 2, 3, 4, 5, 6, 7]
    assert True == True
    assert False == False
    assert None == None
    assert 'a' == 'a'
    assert 'b' != 'a'
    assert 'a' in 'abc'
    assert 'd' not in 'abc'
    assert 1.1 == 1.1
    assert 1.2 != 1.1
    assert 1.3 > 1.2
    assert False is not True
    assert True is True
