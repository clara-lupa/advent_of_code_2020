def parse_file_to_int_list():
    file = open('day1_1_input.txt', 'r').readlines()
    return [int(item) for item in file]

def pair_with_sum(sum, numbers):
    i = 0
    result = False
    for num in numbers:
        for second_num in numbers[i:]:
            if num + second_num == sum:
                result = num * second_num
                print("found")
                print(i)
                print(num)
                print(second_num)
                return result
        # if result != False:
        #     break
        i += 1
        print(i)
    return result

numbers = parse_file_to_int_list()
print (pair_with_sum(2020, numbers))
