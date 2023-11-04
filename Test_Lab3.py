import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_return_1():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 45, 33, 78]  # >= 10 numbers
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 1)

def test_bubble_sort_return_0():
    result = []
    input_arr = []  # 0 numbers
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 0)

def test_bubble_sort_return_2():
    result = []
    input_arr = [12, 2, 33, "four", 65, "six", 37, 78, "nine", 10]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 2)

