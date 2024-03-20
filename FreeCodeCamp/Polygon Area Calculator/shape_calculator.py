class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def set_width(self, new_width):
        self.width = new_width
    
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            line_output = 'abc'
            for symbol_line in range(self.width):
                for symbol_column in range(self.height):
                    '*'.join(line_output)
                '\n'.join(line_output)
            print(line_output)
    
    def get_amount_inside(self, Square):
        pass
    
class Square(Rectangle):
    def __init__(self):
        self.side = Rectangle.width
        
    def set_side(self):
        pass
    
    def set_width(self):
        self.side = Rectangle.width
        
    def set_height(self):
        self.side = Rectangle.height
    


    # def print_all(self):
    #     print(Rectangle.get_area(self))
    #     print(Rectangle.get_perimeter(self))
    #     print(Rectangle.get_diagonal(self))
    #     print(Rectangle.get_picture(self))
        
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
# print(rect.get_amount_inside(sq))