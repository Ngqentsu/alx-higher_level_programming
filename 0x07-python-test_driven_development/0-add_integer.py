def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be first casted to integers if they are float

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
