i = input()
i = int(i)

if i % 3 == 0 and i % 5 == 0:
    print("افسانه ای")
elif i % 3 == 0: 
    print("جادویی")
elif i % 5 == 0: 
    print("نفرین شده")
else:
    print("معمولی")