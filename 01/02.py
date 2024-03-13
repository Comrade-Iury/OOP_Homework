class Button:
    def __init__(self):
        self.__count = 0

    def click(self):
        self.__count += 1

    def click_count(self):
        return self.__count

    def reset(self):
        self.__count = 0
