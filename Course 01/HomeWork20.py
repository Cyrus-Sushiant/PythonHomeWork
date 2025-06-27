def skyline(args):
    result = int(args[0])
    for arg in args:
        i = int(arg)
        if i > result:
            result = i
    return result

user_valuse = input()

if len(user_valuse) < 1 or user_valuse == " ":
    print(0)
else:
    print(skyline(user_valuse.split(" ")))