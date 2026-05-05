import pytest
from semana_16.ejercicio_1 import bubble_sort

def test_bubble_sort_with_small_list():
    #Arrange
    numbers = [5, 2, 4, 1, 3]
    expected_result = [1, 2, 3, 4, 5]
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == expected_result


def test_bubble_sort_with_large_list():
    #Arrange
    numbers = list(range(150, 0, -1))
    expected_result = list(range(1, 151))
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == expected_result


def test_bubble_sort_with_empty_list():
    #Arrange
    numbers = []
    expected_result = []
    #Act
    result = bubble_sort(numbers)
    #Assert
    assert result == expected_result


def test_bubble_sort_with_invalid_input():
    #Arrange
    invalid_input = "not a list"
    #Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(invalid_input)