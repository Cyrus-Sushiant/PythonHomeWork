def sum_numbers(a):
    result = 0
    for arg in a:
        result += int(arg)
    
    return result

user_input = input()

if len(user_input) < 1:
    print(sum_numbers())
else:
    numbers = tuple(user_input.split(" "))
    print(sum_numbers(numbers))