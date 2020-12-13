from day1_1 import *

numbers = parse_file_to_int_list()

def triplet_with_sum(sum, numbers):
    i = 0
    result = False
    for num in numbers:
        pair_product = pair_with_sum(2020 - num, numbers[i:])
        if pair_product!= False:
            return num * pair_product
        i += 1
        print(i)
    return result

print(triplet_with_sum(2020, numbers))
