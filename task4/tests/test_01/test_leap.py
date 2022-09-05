from simple_library_01.functions import is_leap

def test_is_leap():
    try:
        is_leap(-10000)
    except AttributeError:
        assert True
    except:
        assert False

    assert is_leap(2004)

    assert not is_leap(2100)

    assert is_leap(2000)

    assert not is_leap(1999)
