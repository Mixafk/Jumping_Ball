"""Создаём програмудля прыгающих шаров"""


class Ball():
    """Шар родитель, основной класс"""
    # default_diameter = 1
    # default_weight = 1
    default_rigidity = 1
    default_color = 'red'


    def __init__(self, rigidity, InitPos, color):
        """ Initate our ball """
        # self.diameter = diameter
        # self.weight = weight
        self.rigidity = rigidity
        self.InitPos = InitPos
        self.color = color
        

    # def movement(self):
    #     """Шар меняет своё положение в пространстве"""
    #     self.coord_x += vector_x
    #     self.coord_y += vector_y - g
