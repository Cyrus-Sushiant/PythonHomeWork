user_input = int(input())

discount = 0
if user_input > 50000:
    discount = 20
elif 20000 < user_input < 50000:
    discount = 10
else:
    discount = 0

total_payment = user_input
if discount > 0:
    total_payment = user_input - (user_input * discount // 100)

print(total_payment)