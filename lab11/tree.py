class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root


def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)


if __name__ == "__main__":
    tree = None

    tree = insert(tree, 50)
    tree = insert(tree, 30)
    tree = insert(tree, 20)
    tree = insert(tree, 40)
    tree = insert(tree, 70)
    tree = insert(tree, 60)
    tree = insert(tree, 80)

    result = search(tree, 40)
    if result:
        print("Элемент найден")
    else:
        print("Элемент не найден")

    print("In-order обход дерева:")
    inorder_traversal(tree)
