import func as f


width = f.float_val_pos("Введіть довжину прямокутника: ")
height = f.float_val_pos("Введіть висоту прямокутника: ")
side_square = f.float_val_pos("Введіть сторону квадрату: ")
result = (width//side_square)*(height//side_square)
print(result,' квадратів')