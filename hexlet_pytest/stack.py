stack = []  # В питоне стек реализован через список
print(not stack)  # Список пуст
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
print(not stack)  # Список не пустой
print(stack)
stack.pop()  # В стеке [1, 2]
stack.pop()  # В стеке [1]
stack.pop()  # В стеке пусто
print(not stack)