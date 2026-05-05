from semana_16.ejercicio_2 import(
    sum_list,
    reverse_string,
    count_upper_and_lower,
    sort_words_in_string,
    get_primes_from_list,
)

# ------------
# sum_list
# ------------
def test_sum_list_with_positive_numbers():
    #Arrange
    numbers = [15, 8, 16, 4]
    expected_result = 43
    #Act
    result = sum_list(numbers)
    #Assert
    assert result == expected_result


def test_sum_list_with_zeros():
    #Arrange
    numbers = [0, 0, 0]
    expected_result = 0
    #Act
    result = sum_list(numbers)
    #Assert
    assert result == expected_result


def test_sum_list_with_negative_numbers():
    #Arrange
    numbers = [-1, -2, -3]
    expected_result = -6
    #Act
    result = sum_list(numbers)
    #Assert
    assert result == expected_result

# ---------------
# reverse_string
# ---------------
def test_reverse_string_with_normal_text():
    #Arrange
    text = "Mi apodo es Rey"
    expected_result = "yeR se odopa iM"
    #Act
    result = reverse_string(text)
    #Assert
    assert result == expected_result


def test_reverse_string_with_empty_string():
    #Arrange
    text = ""
    expected_result = ""
    #Act
    result = reverse_string(text)
    #Assert
    assert result == expected_result


def test_reverse_string_with_one_character():
    #Arrange
    text = "R"
    expected_result = "R"
    #Act
    result = reverse_string(text)
    #Assert
    assert result == expected_result

# ----------------------
# count_upper_and_lower
# ----------------------
def test_count_upper_and_lower_mixed_text():
    #Arrange
    text = "I love to play Handball"
    expected_result = (2, 17)
    #Act
    result = count_upper_and_lower(text)
    #Assert
    assert result == expected_result


def test_count_upper_and_lower_only_uppercase():
    #Arrange
    text = "ABC"
    expected_result = (3, 0)
    #Act
    result = count_upper_and_lower(text)
    #Assert
    assert result == expected_result


def test_count_upper_and_lower_only_lowercase():
    #Arrange
    text = "python"
    expected_result = (0, 6)
    #Act
    result = count_upper_and_lower(text)
    #Assert
    assert result == expected_result

# ---------------------
# sort_words_in_string
# ---------------------
def test_sort_words_in_string_nornal_case():
    #Arrange
    text = "python-variable-funcion-computadora-monitor"
    expected_result = "computadora-funcion-monitor-python-variable"
    #Act
    result = sort_words_in_string(text)
    #Assert
    assert result == expected_result


def test_sort_words_in_string_two_words():
    #Arrange
    text = "zebra-apple"
    expected_result = "apple-zebra"
    #Act
    result = sort_words_in_string(text)
    #Assert
    assert result == expected_result


def test_sort_words_in_string_already_sorted():
    #Arrange
    text = "apple-banana-watermelon"
    expected_result = "apple-banana-watermelon"
    #Act
    result = sort_words_in_string(text)
    #Assert
    assert result == expected_result

# ---------------------
# get_primes_from_list
# ---------------------
def test_get_primes_from_list_mixed_numbers():
    #Arrange
    numbers = [12, 23, 27, 64, 61, 8, 1]
    expected_result = [23, 61]
    #Act
    result = get_primes_from_list(numbers)
    #Assert
    assert result == expected_result


def test_get_primes_from_list_only_primes():
    #Arrange
    numbers = [2, 3, 5, 7, 11]
    expected_result = [2, 3, 5, 7, 11]
    #Act
    result = get_primes_from_list(numbers)
    #Assert
    assert result == expected_result


def test_get_primes_from_list_not_primes():
    #Arrange
    numbers = [1, 4, 6, 8, 9, 10]
    expected_result = []
    #Act
    result = get_primes_from_list(numbers)
    #Assert
    assert result == expected_result