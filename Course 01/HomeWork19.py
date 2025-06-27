def pick_evens(args):
    result = []
    for arg in args:
        i = int(arg)
        if i % 2 == 0:
            result.append(i)
    
    return result

user_input = input().split(" ")

print(pick_evens(user_input))