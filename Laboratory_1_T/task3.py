"""
Завдання: обчислити згідно формули №22
"""

import math
import func as f


zminna = f.float_val()
if zminna > 1.1:
    print(9-zminna)
elif zminna < -1.1:
    print(math.sin(3*zminna)/(zminna**4+1))
else:
    print('Функція значень не має')
