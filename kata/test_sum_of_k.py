import sum_of_k


def test_sum():
    assert sum_of_k.sum_of_k([10, 2, 5, 6, 3, 5], 15) == True
    assert sum_of_k.sum_of_k([10, 2, 5, 6, 3, 5], 20) == False
    assert sum_of_k.sum_of_k([10, 2, 5, 6, 3, 5], 12) == True
    assert sum_of_k.sum_of_k([10, 2, 5, 6, 3, 5], 18) == False
    assert sum_of_k.sum_of_k([10, 2, 5, 6, 3, 5], 16) == True
