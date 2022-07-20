from imp import is_frozen


def compact(lst):
    non_true = []
    for item in lst:
        if item:
            non_true.append(item)
    return non_true


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
    # """Return a copy of lst with non-true elements removed.

    #     >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    #     [1, 2, 'All done']
    # """