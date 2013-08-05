
def make_iterable(data):
    """
    Turn anything into an iterable object. However, a string
    is already iterable, and I don't want that to return an iterable of
    all the letters. Basically, if what we get is not a list object, I
    want to return a list.
    """

    is_string = isinstance(data, basestring)

    if is_string:
        # if it's a string, turn it into a list so we don't iterate
        # over every letter in the string
        data = [data]
    else:
        # otherwise, find out if it's iterable. if not, make it a list
        try:
            x = iter(data)
        except (NotImplementedError, TypeError):
            data = [data]

    return data
