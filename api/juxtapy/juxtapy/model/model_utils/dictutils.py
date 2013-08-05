from juxtapy.utils import funcs

def build_dict(obj, attrs=None):
    """
    Take an iterable of attrs, and return a dict of the obj.

    If the object has created and/or modified, add it.

    Do the same for the deleted set.

    :param obj: An object to convert to a dictionary.
    :type obj: db.Model

    :param attrs: A list of attributes from the model to put in the dict
    :type attrs: Iterable

    :return: A dictionary representation of the model
    :rtype: dict
    """

    attrs = funcs.make_iterable(attrs)

    ret = {}
    for attr in attrs:
        if attr and hasattr(obj, attr):
            ret[attr] = getattr(obj, attr)

    if hasattr(obj, 'created'):  ret['created']  = format_date(getattr(obj, 'created'))
    if hasattr(obj, 'modified'): ret['modified'] = format_date(getattr(obj, 'modified'))

    if hasattr(obj, 'deleted'):      ret['deleted']      = getattr(obj, 'deleted')
    if hasattr(obj, 'deleted_by'):   ret['deleted_by']   = getattr(obj, 'deleted_by')
    if hasattr(obj, 'deleted_date'): ret['deleted_date'] = format_date(getattr(obj, 'deleted_date'))

    return ret

def format_date(date):
    """
    Return date in a format that the caller would want to deal with. We take a datetime object,
    and return a string.

    :param date: A datetime object to convert to a string.
    :type date: datetime

    :return: ISO8601 string representation of the object
    :rtype: string
    """
    return date.isoformat() if date else None
