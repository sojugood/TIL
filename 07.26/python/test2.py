# ws_7_3.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def print_info(self):
        print(f'Width: {self.width}')
    
shape1 = Shape(5, 3)
shape1.print_info()