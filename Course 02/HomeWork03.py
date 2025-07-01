from itertools import permutations

def solve_yasuj():
    word = "yasuj"
    valid_permutations = []

    # تولید تمام جایگشت‌ها
    for p in permutations(word):
        joined = ''.join(p)
        if joined[0] < joined[-1]:  # بررسی شرط حرف اول و آخر
            valid_permutations.append(joined)

    # چاپ تعداد و لیست جایگشت‌ها (در صورت نیاز)
    print("تعداد جایگشت‌های معتبر:", len(valid_permutations))
    return valid_permutations

# خروجی را در متغیر ذخیره کن
result = solve_yasuj()
# نمایش آیتم ها
print(result)
