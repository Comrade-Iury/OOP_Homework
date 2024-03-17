class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x0, self.__y0, self.__width, self.__height = x, y, width, height
        self.__x1, self.__y1 = x + width, y + height

    def intersection(self, other):
        if self.__x0 >= other.__x0 and self.__y0 >= other.__y0 and self.__x1 <= other.__x1 and self.__y1 <= other.__y1:
            return self
        if self.__x0 <= other.__x0 and self.__y0 <= other.__y0 and self.__x1 >= other.__x1 and self.__y1 >= other.__y1:
            return other
        if self.__x0 < other.__x0 < self.__x1 and self.__y0 < other.__y0 < self.__y1:
            x, y = other.__x0, other.__y0
            width = self.__x1 - other.__x0
            height = self.__y1 - other.__y0
            return Rectangle(x, y, width, height)
        if other.__x0 < self.__x0 < other.__x1 and other.__y0 < self.__y0 < other.__y1:
            x, y = self.__x0, self.__y0
            width = other.__x1 - self.__x0
            height = other.__y1 - self.__y0
            return Rectangle(x, y, width, height)
        return None

    def get_x(self):
        return self.__x0

    def get_y(self):
        return self.__y0

    def get_h(self):
        return self.__height

    def get_w(self):
        return self.__width
