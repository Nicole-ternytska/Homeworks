import func as f

varA = f.int_val_A('Введіть число А (>1): ')

sum = 0
iter = 1
while sum < varA:
    sum += 1/iter
    iter += 1
print("Значення К = ", iter-1)
print("Сума = ", sum)
