def same_frequency(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


    # """Do these nums have same frequencies of digits?
    
print(same_frequency(551122, 221515))
        # True
        
print(same_frequency(321142, 3212215))
        # False
        
print(same_frequency(1212, 2211))
        # True
