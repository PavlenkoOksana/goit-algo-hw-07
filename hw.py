class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# Завдання 1: Функція, яка знаходить найбільше значення у двійковому дереві пошуку.

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


# Завдання 2: Функція, яка знаходить найменше значення у двійковому дереві пошуку. 

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Завдання 3: Функція, яка знаходить суму всіх значень у двійковому дереві пошуку. 

def sum_value_node(node, current_sum=0):
    if node:
        current_sum += node.val
        current_sum = sum_value_node(node.left, current_sum)
        current_sum = sum_value_node(node.right, current_sum)
    return current_sum


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 0)


root = delete(root, 8)
print(root)
print("Найбільше значення у двійковому дереві пошуку: ", max_value_node(root))
print("Найменше значення у двійковому дереві пошуку: ", min_value_node(root))
print("Сума всіх значень у двійковому дереві пошуку: ", sum_value_node(root))