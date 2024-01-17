def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it should return False
    if the number of even numbers is odd, it should return False
    if the number of even numbers is 0, it should return False
    if the number of even numbers is even, it should return True
    """
    if isinstance(numbers, list):
        evens = 0
        for number in numbers:
            if number % 2 == 0:
                evens += 1
        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == "__main__":
    print(even_number_of_evens(5))
