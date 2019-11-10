import func as f
zminna_x = f.float_val_notone('Введіть значення Х ')
n = f.int_val_N("Введіть значення n ")
summa = 0

for i in range(1, n + 1):
    summa += (2 * zminna_x + 1) ** i / (zminna_x - 1)
print(summa)