import func as f


x_A = f.int_val('Введіть координату X точки А: ')
y_A = f.int_val('Введіть координату Y точки А: ')
x_B = f.int_val('Введіть координату Х точки B: ')
y_B = f.int_val('Введіть координату Y точки B: ')
x_C = f.int_val('Введіть координату Х точки C: ')
y_C = f.int_val('Введіть координату Y точки C: ')
x_D = f.int_val('Введіть координату Х точки D: ')
y_D = f.int_val('Введіть координату Y точки D: ')
averageX1 = (x_A + x_C) / 2
averageY1 = (y_A + y_C) / 2
averageX2 = (x_B + x_D) / 2
averageY2 = (y_B + y_D) / 2
if averageX1 == averageX2 and averageY2 == averageY1:
    print('Точки є вершинами паралелограму')
else:
    print('Точки не є верш