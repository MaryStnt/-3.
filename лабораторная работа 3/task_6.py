list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_num = 0
for i in range(len(list_numbers)):
    max_ = list_numbers[max_num]
    current = list_numbers[i]
    if current > max_:
        max_num = i

list_numbers[max_num], list_numbers[-1] = list_numbers[-1], list_numbers[max_num]
print(list_numbers)



