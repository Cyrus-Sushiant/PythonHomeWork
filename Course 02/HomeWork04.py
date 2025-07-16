import random

def generate_single_number():
    r = random.random()
    if r < 0.6:
        return random.randint(1, 4)  # اعداد 1 تا 4 با احتمال 60٪
    else:
        return 5  # عدد 5 با احتمال 40٪

def generate_single_person_numbers():
    return [generate_single_number() for _ in range(5)]

def run_experiment(num_people=100):
    all_numbers = [generate_single_person_numbers() for _ in range(num_people)]
    total_sum = sum(sum(person) for person in all_numbers)
    total_count = num_people * 5
    average = total_sum / total_count
    return average, all_numbers

# اجرای شبیه‌سازی
average, data = run_experiment()

# چاپ خروجی
print(round(average, 2))  # فقط میانگین با دقت دو رقم اعشار
print(data)               # لیست صدتایی هرکدام شامل ۵ عدد
