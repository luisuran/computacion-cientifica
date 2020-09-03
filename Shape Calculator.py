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
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        imagen = ""

        for x in range(self.height):
            imagen += "*" * self.width + "\n"
        
        return imagen

    def get_amount_inside(self, forma):
        cant_ancho = int(self.width / forma.width)
        cant_alto = int(self.height / forma.height)

        return cant_alto * cant_ancho

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, lado):
        self.width = lado
        self.height = lado

    def set_width(self, lado):
        self.set_side(lado)

    def set_height(self, lado):
        self.set_side(lado)

    def set_side(self, lado):
        self.width = lado
        self.height = lado

    def __str__(self):
        return "Square(side={})".format(self.width)