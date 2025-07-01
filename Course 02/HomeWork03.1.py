counter = 0
for i in range(10, 100):
    if i % 2 == 0:
        if len(set(str(i))) == 2:
            counter += 1

print(counter)
