"""Создаём програмудля прыгающих шаров"""
from Vector import Vector

class Ball():
    """Шар родитель, основной класс"""
    # default_diameter = 1
    # default_weight = 1
    default_rigidity = 1
    default_color = 'red'


    def __init__(self, rigidity, init_pos_x, init_pos_y, speed_dir_x, speed_dir_y, color):
        """ Initate our ball """
        # self.diameter = diameter
        # self.weight = weight
        self.rigidity = rigidity
        self.init_pos = Vector(init_pos_x, init_pos_y)
        self.speed_dir = Vector(speed_dir_x, speed_dir_y)
        self.color = color
    
    def show_Ball(self):
        """Показать характеристики шара"""
        print(f'Жёсткость (прыгучесть) шара - {self.rigidity}')
        print(f'Координаты шара: (x0={self.init_pos.initial_x}, y0={self.init_pos.initial_y})')
        print(f'Вектор скорости: x={self.speed_dir.initial_x}, y={self.speed_dir.initial_y}')
        print()

    def set_speed_dir(self, new_speed_dir_x, new_speed_dir_y):
        """Устанавливаем новый родной вектор скорости шара"""
        self.speed_dir.initial_x = new_speed_dir_x
        self.speed_dir.initial_y = new_speed_dir_y
        print()  

    def movement(self):
        """Шар меняет своё положение в пространстве"""
        self.init_pos_x.initial_x += self.speed_dir_x.initial_x
        self.init_pos_y.initial_y += self.speed_dir_y.initial_y - 1
        print(f'Координаты шара теперь: (x0={self.init_pos_x}, y0={self.init_pos_y})')
        print()


sha = Ball(1, 2, 2, 3, 3, 'yellow')

sha.show_Ball()

dae = Vector(1, 3)

sha.set_speed_dir(1, 3)

sha.show_Ball()
