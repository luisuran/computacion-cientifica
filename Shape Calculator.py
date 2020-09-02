class Rectangle:
    width = 0
    height = 0

    def __init__(self, ancho, alto):
        self.width = ancho
        self.height = alto

    def set_width(self, n):
        self.width = n

    def set_height(self, n):
        self.height = n

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        imagen = ""

        for x in range(self.height):
            imagen += "*" * self.width + "\n"
        
        return imagen

    def get_amount_inside(self, forma):
        if type(r1).__name__ == 'Rectangle':
            lado = min(forma.height, forma.width)
        else:
            lado = forma.lado

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    lado = 0

    def __init__(self, lado):
        self.lado = lado

    def set_width(self, n):
        self.width = n

    def set_height(self, n):
        self.height = n

    def __str__(self):
        return "Square(side={})".format(self.lado)