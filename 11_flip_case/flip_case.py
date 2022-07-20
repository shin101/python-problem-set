def flip_case(phrase, to_swap):
    flipped = ''
    for char in phrase:
        if char == to_swap.lower() or to_swap.upper():
            if char == char.lower():
                char = char.swapcase()
                flipped+=char
            else:
                char == char.lower()
                char = char.swapcase()
                flipped+=char
    return flipped
            



print(flip_case('Aaaahhh', 'h'))

    # """Flip [to_swap] case each time it appears in phrase.

    #     >>> flip_case('Aaaahhh', 'a')
    #     'aAAAhhh'

    #     >>> flip_case('Aaaahhh', 'A')
    #     'aAAAhhh'

    #     >>> flip_case('Aaaahhh', 'h')
    #     'AaaaHHH'

    # """
