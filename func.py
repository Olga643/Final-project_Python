# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни
#Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

limit = 10
step = 0.001
color = 'b'
line_s = '-'
direct_up = True

x = np.arange(-limit, limit, step)

def switch_line():
    global line_s
    if line_s == '-':
        line_s = '--'
    else:
        line_s = '-'
    return line_s

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color


a, b, c, d, e = -12, -18, 5, 10, -30

def func(x):
    return a * x**4 * np.sin(np.cos(x)) + b * x**3 + c * x**2 + d * x + e

x_change = [(-limit, 'limit')]
for i in range(len(x) - 1):
    if (func(x[i]) > 0 and func(x[i+1]) < 0) or (func(x[i]) < 0 and func(x[i+1]) > 0):
        x_ac = np.arange(x[i], x[i+1], 0.000001)
        for j in range(len(x_ac) - 1):
            if (func(x_ac[j]) > 0 and func(x_ac[j+1]) < 0) or (func(x_ac[j]) < 0 and func(x_ac[j+1]) > 0):
                x_change.append((x_ac[j] if abs(0 - x_ac[j]) < abs(0 - x_ac[j+1]) else x_ac[j+1] , 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i+1]):
           x_change.append((x[i], 'direct'))
           direct_up = False
    else:
         if func(x[i]) < func(x[i+1]):
           x_change.append((x[i], 'direct'))
           direct_up = True
x_change.append((limit, 'limit'))

print(x_change)

for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i+1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())


min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct' or 'limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]


roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')

plt.plot(min_x, min_y, 'yo', label = f'Экстремум фунции на промежутке [{-limit};{limit}]: {min_x}, {min_y}')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label = 'Убывание > 0')
plt.plot(0, 0, 'r', label = 'Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label = 'Убывание < 0')
plt.plot(0, 0, 'r', label = 'Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.grid()
plt.show()
