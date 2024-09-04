import main_file as source


def test_get_square_area_1():
    assert source.get_square_area(3) == 9


def test_get_square_area_2():
    assert source.get_square_area(7) == 49


def test_get_square_perimeter_1():
    assert source.get_square_perimeter(3) == 12


def test_get_square_perimeter_2():
    assert source.get_square_perimeter(7) == 28
   