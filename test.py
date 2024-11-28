def sum_num(num_str: str):
    num_list = num_str.split('a')
    return sum(list(map(int, num_list)))


number_str = '1b2a3a4a5'

def sum_num_2(num_str: str):
    sum_number = 0
    for i in range(len(num_str)):
        if num_str[i].isdigit():
            sum_number += int(num_str[i])
    return sum_number

print(sum_num_2(number_str))