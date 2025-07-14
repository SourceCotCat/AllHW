
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return len(self.__items) == 0

    def push(self, item):
        """Добавляет новый элемент."""
        self.__items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека, иначе возвращает None."""
        if self.is_empty():
            return None
        return self.__items.pop()

    def peek(self):
        """Возвращает верхний элемент стека, не удаляя его, иначе возвращает None."""
        if self.is_empty():
            return None
        return self.__items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.__items)