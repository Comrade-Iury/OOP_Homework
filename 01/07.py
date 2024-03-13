class BoundingRectangle:
    def __init__(self):
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.is_first = True

    def add_point(self, x, y):
        if self.is_first:
            self.min_x, self.max_x = x, x
            self.min_y, self.max_y = y, y
            self.is_first = False
        else:
            if y < self.min_y:
                self.min_y = y
            elif y > self.max_y:
                self.max_y = y
            if x < self.min_x:
                self.min_x = x
            elif x > self.max_x:
                self.max_x = x

    def width(self):
        if self.max_x <= 0:
            return abs(self.min_x) - abs(self.max_x)
        if self.min_x < 0 < self.max_x:
            return abs(self.min_x) + self.max_x
        if self.min_x > 0:
            return self.max_x - self.min_x

    def height(self):
        if self.max_y <= 0:
            return abs(self.min_y) - abs(self.max_y)
        if self.min_y < 0 < self.max_y:
            return abs(self.min_y) + self.max_y
        if self.min_y > 0:
            return self.max_y - self.min_y

    def bottom_y(self):
        return self.min_y

    def top_y(self):
        return self.max_y

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x


rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
