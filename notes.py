# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog: 
    #functions that start with __ are not intended to be called directly
    def __init__(self, fc = "", a = 0, w = 0.0, n = "") -> None:
        """Create an instance of the do class and set attributes"""
        self.fur_color = fc
        self.age = a
        self.weight = w
        self.name = n
        self.fetch_count = 0

    def _str_(self)

        
        

