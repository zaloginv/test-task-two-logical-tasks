N_and_M = input('Числа N и M через пробел: ')
N, M = N_and_M.split(' ')
N = int(N)
M = int(M)

string_N = ''

for number in range(N):
    number += 1
    string_N += str(number)

list_of_list_of_numbers = []


def sorting(work_string, start_string=[]):
    string_len = len(work_string)

    if string_len > 1:
        for index in range(1, string_len):
            left_string = work_string[:index]
            right_string = work_string[index:]

            result_left_string = [*start_string, left_string]
            listing = [*result_left_string, right_string]

            list_of_list_of_numbers.append(listing)
            sorting(work_string=right_string, start_string=result_left_string)


sorting(work_string=string_N)


for list_of_numbers in list_of_list_of_numbers:
    sum_result = 0
    for str_number in list_of_numbers:
        sum_result += int(str_number)

    if sum_result == M:
        result_string = f'{"+".join(list_of_numbers)}={M}'
        print(result_string)