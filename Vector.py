

class Vector():
    """Создаём любой вектор"""

    def __init__(self, initial_x, initial_y, finite_x, finite_y):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.finite_x = finite_x
        self.finite_y = finite_y
        
    
    def show_vector(self):
        print(f'Начальные координаты: (x0={self.initial_x}, y0={self.initial_y})')
        print(f'Начальные координаты: (x0={self.finite_x}, y0={self.finite_y})')
        print()

    def set_x(self, new_initial_x, new_finite_x):
        """Задать новые начальные и коенчные координаты Х вектора"""
        self.initial_x = new_initial_x
        self.finite_x = new_finite_x
    
    def set_y(self, new_initial_y, new_finite_y):
        """Задать новые начальные и коенчные координаты Y вектора"""
        self.initial_y = new_initial_y
        self.finite_y = new_finite_y

    def vector_length(self):
        """Показать длину вектора"""
        print(f'Длина вектора: {round(float(((self.finite_x - self.initial_x)**2 + (self.finite_y - self.initial_y)**2)**0.5), 2)}')

    def sum_vectors(self, initial_x2, initial_y2, finite_x2, finite_y2):
        """Прибавить вектор к существующему"""
        self.finite_x += finite_x2 - initial_x2
        self.finite_y += finite_y2 - initial_y2

    def diff_vectors(self, initial_x2, initial_y2, finite_x2, finite_y2):
        """Вычесть вектор из существующего"""
        self.initial_x += finite_x2 - initial_x2
        self.initial_y += finite_y2 - initial_y2

    def mult_vector(self, factor):
        """Умножить вектор на число"""
        self.finite_x = self.initial_x + (self.finite_x - self.initial_x) * factor
        self.finite_x = self.initial_y + (self.finite_y - self.initial_y) * factor
        


kuka = Vector(1, 1, 5, 5)
