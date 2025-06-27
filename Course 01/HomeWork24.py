def time_decorator(func):
    def wrapper(*args, **kw):
        import time
        start_time = time.time() 

        result = func(*args, **kw)

        end_time = time.time()
        print("execute time: %2.6f sec, args: %s" %(end_time-start_time, args))

        return result

    return wrapper

@time_decorator
def create_list(n):
    result = []
    start_num = 1
    while (start_num <= n):
        result.append(start_num)
        start_num += 1
    
    return result

numbers = create_list(10000)

print(numbers)