n = input("Enter n:")
ali_nums = input("Enter Ali's numbers:")
ali_fiance_nums = input("Enter Ali's fiance's numbers:")

ali_set_nums = set(ali_nums.split())
ali_fiance_set_nums = set(ali_fiance_nums.split())

#Ali and his fiance share similar characteristics 
a_f_intersection = ali_set_nums.intersection(ali_fiance_set_nums)

#Ali and his fiance share the same number of characteristics.
l = len(a_f_intersection)
r = int(n) // 2


if (l > r):
    print("YES")
else:
    print("NO")
