# Реализация стека
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == [] # возвращает True, если стек пустой, иначе False

    def push(self, item):
        self.items.append(item) # добавление элемента в стек

    def pop(self):
        return self.items.pop() # удаление и возврат верхнего элемента из стека

    def peek(self):
        return self.items[-1] # получение верхнего элемента без его удаления

    def size(self):
        return len(self.items) # возвращает количество элементов в стеке

# Пример использования стека
stack = Stack()
print(stack.is_empty()) # выводится значение True, так как стек изначально пуст
stack.push(1)           # добавление элемента 1 в стек
stack.push(2)           # добавление элемента 2 в стек
stack.push(3)           # добавление элемента 3 в стек
print(stack.is_empty()) # выводится значение False, так как стек не пуст
print(stack.peek())     # выводится верхний элемент (3), без удаления
print(stack.pop())      # удаляется и выводится верхний элемент (3)
print(stack.peek())     # выводится новый верхний элемент (2)

# Реализация очереди
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == [] # возвращает True, если очередь пустая, иначе False

    def enqueue(self, item):
        self.items.insert(0, item) # добавление элемента в конец очереди

    def dequeue(self):
        return self.items.pop() # удаление и возврат элемента из начала очереди

    def size(self):
        return len(self.items) # возвращает количество элементов в очереди

# Пример использования очереди
queue = Queue()
print(queue.is_empty())        # выводится значение True, так как очередь изначально пустая
queue.enqueue("Task 1")       # добавление элемента "Task 1" в очередь
queue.enqueue("Task 2")       # добавление элемента "Task 2" в очередь
queue.enqueue("Task 3")       # добавление элемента "Task 3" в очередь
print(queue.is_empty())        # выводится значение False, так как очередь не пустая
print(queue.size())            # выводится размер очереди (3)
print(queue.dequeue())         # удаляется и выводится первый элемент очереди ("Task 1")
print(queue.size())            # выводится новый размер очереди (2)

# Реализация бинарного дерева поиска
class Node:
    def __init__(self, key):
        self.left = None       # левая ветвь узла
        self.right = None      # правая ветвь узла
        self.val = key         # значение узла

def insert(root, key):
    if root is None:
        return Node(key)       # создается новый узел, если корневой отсутствует
    else:
        if root.val < key:     # добавление узла в правую ветвь, если значение больше
            root.right = insert(root.right, key)
        else:                  # добавление узла в левую ветвь, если значение меньше или равно
            root.left = insert(root.left, key)
    return root

# Пример использования бинарного дерева поиска
root = Node(50)               # создание корневого узла со значением 50
root = insert(root, 30)       # добавление узла со значением 30
root = insert(root, 70)       # добавление узла со значением 70
root = insert(root, 20)       # добавление узла со значением 20
root = insert(root, 40)       # добавление узла со значением 40
root = insert(root, 60)       # добавление узла со значением 60
root = insert(root, 80)       # добавление узла со значением 80

# Функция для обхода дерева (in-order)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left) # рекурсивный вызов для левой ветви
        print(root.val, end=" ")    # вывод значения текущего узла
        inorder_traversal(root.right) # рекурсивный вызов для правой ветви

print("In-order traversal of the tree:")
inorder_traversal(root)       # обход дерева и вывод значений в порядке in-order

# Реализация графа
class Graph:
    def __init__(self):
        self.graph = {}       # инициализация графа в виде словаря

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [] # если узла u нет в графе, создается пустой список связей
        self.graph[u].append(v) # добавление узла v в список связей узла u

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node]))) # вывод узлов и их связей

# Пример использования графа
g = Graph()
g.add_edge(0, 1)              # добавление связи между узлами 0 и 1
g.add_edge(0, 4)              # добавление связи между узлами 0 и 4
g.add_edge(1, 2)              # добавление связи между узлами 1 и 2
g.add_edge(1, 3)              # добавление связи между узлами 1 и 3
g.add_edge(1, 4)              # добавление связи между узлами 1 и 4
g.add_edge(2, 3)              # добавление связи между узлами 2 и 3
g.add_edge(3, 4)              # добавление связи между узлами 3 и 4

g.print_graph()               # вывод графа с узлами и их связями
