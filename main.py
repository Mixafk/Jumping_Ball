from Vector import Vector
from Ball import Ball
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np


def is_ball_stoped(nums):
    return all(list(map(lambda x: x < 1, nums)))


kuka = Ball(50, 100, -15, 20, 1)
x_kuka = [kuka.pos.x]
y_kuka = [kuka.pos.y]
kuka.show_Ball()

while is_ball_stoped(y_kuka[-3:]) == False:
# for _ in range(10):
    # print(len(x_kuka))
    # kuka.bounce()
    kuka.move()
    # kuka.bounce()
    x_kuka.append(kuka.pos.x)
    y_kuka.append(kuka.pos.y)
    kuka.show_Ball()
    # print(y_kuka[-3:])
    

print(x_kuka)
print(y_kuka)

x = x_kuka
y = y_kuka
# y2 = [i**2 for i in x]
plt.title('Движение шаров') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.grid() # включение отображение сетки
plt.plot(x, y, 'o--r', label='ball_1') # построение графика
# plt.plot(x, y2, 'b--', label='ball_2')
plt.legend(['ball_1']) # создание легенды
plt.legend(loc='best') # лучшее расположение для легенды
plt.show() # построение


