""" 
Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in. """

def add_it_up(number):
    check = 0
    for i in range(number):
        if i < number:
            i += 1
        check += i
    return check

number = int(input('Enter the number: '))
print(add_it_up(number))


def same_function_as_formula(number):
    s = number * (number + 1)/2
    return s

print(same_function_as_formula(number))
