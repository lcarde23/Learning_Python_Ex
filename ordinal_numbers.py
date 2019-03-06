
numbers = [i for i in range (1,10)]
print(numbers)

for value in numbers:
    if value == 1:
        print(str(value) + 'st\n')

    elif value == 2:
        print(str(value) + 'nd\n')

    elif value == 3:
        print(str(value) + 'rd\n')

    else:
        print(str(value) + 'th\n')