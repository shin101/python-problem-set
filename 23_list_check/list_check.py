def list_check(lst):
    for item in lst:
        if not isinstance(item,list):
            return False
    return True

    # """Are all items in lst a list?
    # """

print(list_check([[1], [2, 3]]))
        # True

print(list_check([[1], "nope"]))
        # False