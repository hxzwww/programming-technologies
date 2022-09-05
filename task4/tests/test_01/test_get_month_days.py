from simple_library_01.functions import get_month_days

def test_get_month_days():
    for i in range(1, 13):
        assert 30 == get_month_days(1930, i)

    assert 29 == get_month_days(2004, 2)
    
    assert 29 == get_month_days(2000, 2)

    assert 28 == get_month_days(2003, 2)

    assert 28 == get_month_days(2100, 2)

    for i in [4, 6, 9, 11]:
        assert 30 == get_month_days(1999, i)

    for i in [1, 3, 5, 7, 8, 10, 12]:
        assert 31 == get_month_days(2000, i)

    try:
        get_month_days(2000, 13)
    except AttributeError:
        assert True
    except:
        assert False
