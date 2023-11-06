from Vector import Vector

"""Создаём програмудля прыгающих шаров"""

class Ball():
    """Шар родитель, основной класс"""
    # default_diameter = 1
    # default_weight = 1
    elasticity = 1
    g = 10
    color = 'red'


    def __init__(self, x, y, s_x, s_y, elasticity):
        """ Initate our ball """
        # self.diameter = diameter
        # self.weight = weight
        self.elasticity = elasticity
        self.pos = Vector(x, y)
        self.speed = Vector(s_x, s_y)


    def update(self):
        """Обновить параметры внешней среды"""
        self.add_gravity()


    def add_gravity(self):
        """Изменить значение g гравитации"""
        self.speed.y -= self.g
    

    def show_Ball(self):
        """Показать характеристики шара"""
        print(f'Прыгучесть шара: {self.elasticity}')
        print(f'Координаты шара: (x0={self.pos.x}, y0={self.pos.y})')
        print(f'Вектор скорости: x={self.speed.x}, y={self.speed.y}')
        print()


    def set_speed_dir(self, new_s_x, new_s_y):
        """Устанавливаем новый родной вектор скорости шара"""
        self.speed.x = new_s_x
        self.speed.y = new_s_y
        print()


    # def bounce(self):
    #     if self.pos.x < 0:
    #         self.pos.x = 0
    #         self.speed.x *= -0.5 #* self.elasticity
    #     elif self.pos.y < 0:
    #         self.pos.y = 0
    #         self.speed.y = - self.speed.y / 5 #* self.elasticity

    



    def move(self):
        """Шар меняет своё положение в пространстве"""
        self.speed.y -= self.g
        if self.pos.x + self.speed.x <= 0:
            self.pos.x = 0
            self.speed.x *= -self.elasticity
        else:
            self.pos.x += self.speed.x
        # print(self.pos.y, self.speed.y)
        if self.pos.y + self.speed.y <= 0:
            self.pos.y = 0
            self.speed.y *= -self.elasticity
        else:
            self.pos.y += self.speed.y
        
        print(f'Координаты шара теперь: (x0={self.pos.x}, y0={self.pos.y})')
        print()
    

   

