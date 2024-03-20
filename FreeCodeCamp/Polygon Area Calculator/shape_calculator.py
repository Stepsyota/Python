class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return (f'Rectangle(width={self.width}, height={self.height})')
        
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
            for symbol_column in range(self.height):
                for symbol_line in range(self.width):
                    print('*', end = '')
                print('')
            return ''
    
    def get_amount_inside(self, Square):
        R_width = self.width
        R_height = self.height
        S_width = Square.width
        S_height = Square.height
        side = Square.side
        i = 1
        while S_width < R_width and S_height < R_height:
            if R_width > S_width:
                S_width += S_width
                i+=1
            if R_height > S_height:
                S_height += S_height
                i+=1
            if R_width == S_width and R_height != S_height:
                pass
            if R_width != S_width and R_height == S_height:
                pass
        return i
            
    
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side
        
    def __str__(self):
        return (f'Square(side={self.side})')
        
    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side
    
    def set_width(self, width):
        self.side = width
        self.width = width
        self.height = width
        
    def set_height(self, height):
        self.side = height
        self.width = height
        self.height = height
    
               
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

rect = Rectangle(8,4)
sq = Square(4)
print(rect.get_amount_inside(sq))