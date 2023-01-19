# massive = input('Ввод массива: ')
massive = '-0, 0, 0, 0, 0, 6, 7, 0, 0'
massive_list = massive.split(', ')

list_of_tuples = []

for index_i, number_i in enumerate(massive_list):
    max_number = number_i
    start_index = index_i
    end_index = index_i

    for index_j, number_j in enumerate(massive_list):
        if (index_i < index_j) and (number_j > max_number) and (index_j - end_index == 1):
            max_number = number_j
            end_index = index_j

    list_of_tuples.append((start_index, end_index))


max_difference = 0
result = (0, 0)

for two_numbers in list_of_tuples:
    difference = two_numbers[1] - two_numbers[0]
    if difference > max_difference:
        max_difference = difference
        result = two_numbers

print(*result, sep=', ')
