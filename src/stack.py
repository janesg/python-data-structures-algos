from linked_list import LinkedList


class Stack:
    def __init__(self, initial_value=None):
        self.__ll = LinkedList(initial_value)

    def push(self, value):
        # Adding to 'head' is O(1)
        #   - adding to 'tail' is also O(1)
        return self.__ll.prepend(value)

    def pop(self):
        # Removing from 'head' is O(1)
        #   - removing from 'tail' is a worse option as it is O(n)
        return self.__ll.pop_first()

    def height(self):
        return self.__ll.length

    def print_stack(self):
        self.__ll.print_linked_list()


if __name__ == '__main__':
    stack = Stack()
    print(stack.height())
    print(stack.pop())
    stack = Stack(56)
    print(stack.height())
    print(stack.pop())
    stack.print_stack()
    stack.push('Eric')
    stack.push('Bob')
    stack.push('Nigel')
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.print_stack()

