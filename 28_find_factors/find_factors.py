def find_factors(num):
    # output = []
    # for i in range (1,num+1):
    #     if num%i==0:
    #         output.append(i)

    output = [i for i in range(1,num+1) if num%i==0]
    output.append(num)

    return output


    # """Find factors of num, in increasing order.

print(find_factors(10))
# [1, 2, 5, 10]

print(find_factors(11))
# [1, 11]

print(find_factors(111))
# [1, 3, 37, 111]

print(find_factors(321421))
# [1, 293, 1097, 321421]

