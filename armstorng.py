for num in range(1, 1000):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit *len(str(num))   
        temp //= 10
    if total==num:
        print(num)
