class BinarySearchTree:
    def __init__(self, initial_value=None):
        self.__root = None

        if initial_value is not None:
            self.__root = BinarySearchTree.__Node(initial_value)

    def insert(self, value):
        if self.__root is None:
            self.__root = BinarySearchTree.__Node(value)
            return True

        temp = self.__root
        while temp is not None:
            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = BinarySearchTree.__Node(value)
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = BinarySearchTree.__Node(value)
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.__root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False

    def min_value(self, node=None):
        if node is None:
            node = self.__root

        if node is None:
            return None

        temp = node
        while temp.left is not None:
            temp = temp.left

        return temp.value

    def max_value(self, node=None):
        if node is None:
            node = self.__root

        if node is None:
            return None

        temp = node
        while temp.right is not None:
            temp = temp.right

        return temp.value

    def print_root(self):
        self.__print_node(self.__root)

    @staticmethod
    def __print_node(node):
        print("{} <-- {} --> {}".format(node.left.value, node.value, node.right.value))

    class __Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


if __name__ == '__main__':

    tree = BinarySearchTree()
    print("Min value: {}".format(tree.min_value()))
    print(tree.contains(2))
    tree.insert(25)
    print(tree.insert(13))
    print(tree.insert(13))
    tree.insert(46)
    tree.insert(18)
    tree.insert(14)
    tree.insert(20)
    tree.insert(53)
    tree.insert(4)
    tree.insert(40)
    tree.insert(41)
    tree.insert(43)
    tree.print_root()

    print(tree.contains(13))
    print(tree.contains(42))
    print("Min value: {}".format(tree.min_value()))
    print("Max value: {}".format(tree.max_value()))
