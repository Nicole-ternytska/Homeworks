"""
Завдання: 22) Дано число A(>1). Вивести найменше із цілих чисел K, для яких сума 1+1/2+...+1/K буде більше A, і саму цю суму
"""
import func as f

varA = f.int_val_A('Введіть число А (>1): ')

sum = 0
iter = 1
while sum < varA:
    sum += 1/iter
    iter += 1
print("Значення К = ", iter-1)
print("Сума = ", sum)
