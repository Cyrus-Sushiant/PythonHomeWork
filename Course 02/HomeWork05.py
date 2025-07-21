from pprobs.simulation import Simulator

# 1) ساخت یک شبیه‌ساز جدید
space = Simulator()

# 2) تعریف احتمال اینکه یک فرد دزد باشد
space.add_event('D', 0.01)

# 3) تعریف احتمال مثبت شدن تست پلیس در صورت واقعی بودن دزد
space.add_event('Positive|D', 0.9)

# 4) تعریف احتمال مثبت کاذب (فرد غیرمجرم ولی تست مثبت)
space.add_event('Positive|D!', 0.096)

# 5) محاسبه احتمال واقعی بودن دزد، اگر تست مثبت شود
prob = space.get_prob('D|Positive')

# 6) خروجی سازمان‌یافته
print(f"P(D | Positive) = {prob:.4f}")  
# → P(D | Positive) = 0.0865