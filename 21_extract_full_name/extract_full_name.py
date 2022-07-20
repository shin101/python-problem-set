def extract_full_names(people):
    output = []
    for person in people:
        output.append(person['first'] + ' ' + person['last'])
    return output 


# Return list of names, extracting from first+last keys in people dicts.

#     - people: list of dictionaries, each with 'first' and 'last' keys for
#               first and last names

#     Returns list of space-separated first and last names.

names = [{'first': 'Ada', 'last': 'Lovelace'}, {'first': 'Grace', 'last': 'Hopper'}]

print(extract_full_names(names))
        # ['Ada Lovelace', 'Grace Hopper']
 