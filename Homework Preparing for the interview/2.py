
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


def is_balanced(brackets):
    """
    Проверяет сбалансированность скобок в строке.
    Args: Строка со скобками 
    Returns:  "Сбалансированно" или "Несбалансированно"
    """
    stack = Stack()

    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    opening_br = set(pairs.keys())
    closing_br = set(pairs.values())
    
    for char in brackets:
        if char in opening_br:
            # Если открывающая скобка добавляем 
            stack.push(char)
        elif char in closing_br:
            # Если закрывающая скобка
            if stack.is_empty():
                # Нет соответствующей открывающей скобки
                return "Несбалансированно"
            
            last_opening = stack.pop()
            if pairs[last_opening] != char:
                return "Несбалансированно"
    
    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    print("Введите строку для проверки:")
    user_input = input()
    result = is_balanced(user_input)
    print(result)