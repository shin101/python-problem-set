def vowel_count(phrase):
    phrase = phrase.lower()
    vowels = 'aeiou'
    counter = {}
    for char in phrase:
        if char in vowels:
            counter[char] = counter.get(char,0)+1

        # if char==' ':
        #     char.replace(' ','')
    return counter





# "Return frequency map of vowels, case-insensitive.

print(vowel_count('rithm school'))
        # {'i': 1, 'o': 2}
        
print(vowel_count('HOW ARE YOU? i am great!') )
        # {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
