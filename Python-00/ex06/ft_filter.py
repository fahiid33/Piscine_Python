def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None, return the items that are true
    """

    if iterable is None:
        raise TypeError("'NoneType' object is not iterable")
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))


if __name__ == "__main__":
    def is_even(num):
        return num % 2 == 0

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        even_numbers = ft_filter(is_even, numbers)
        even_numbers_list = list(even_numbers)
        print(even_numbers_list)
        truthy_values = ft_filter(None, None)
        truthy_values_list = list(truthy_values)
        print(truthy_values_list)
    except TypeError as e:
        print("TypeError:", e)

print(ft_filter.__doc__)
