def repeat(phrase, num):
    if isinstance(num,int) and num>=0:
        return phrase*num
    else: 
        return None

    # """Return phrase, repeated num times.

print(repeat('*', 3))
        # '***'

print(repeat('abc', 2))
        # 'abcabc'

print(repeat('abc', 0))
        # ''

    #Ignore illegal values of num and return None:

print(repeat('abc', -1))
# is None
  

print(repeat('abc', 'nope'))
# is None


