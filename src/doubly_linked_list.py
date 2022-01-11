class DoublyLinkedList:
    def __init__(self, initial_value=None):
        self.__head = None
        self.__length = 0

        if initial_value is not None:
            self.__head = DoublyLinkedList.__Node(initial_value)
            self.__length = 1

        self.__tail = self.__head

    @property
    def length(self):
        return self.__length

    def append(self, value):
        new_node = DoublyLinkedList.__Node(value)
        if self.__length == 0:
            self.__tail = new_node
            self.__head = self.__tail
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

        self.__length += 1
        return True

    def prepend(self, value):
        new_node = DoublyLinkedList.__Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = self.__head
        else:
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node

        self.__length += 1
        return True

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.__length:
            return self.append(value)
        else:
            new_node = DoublyLinkedList.__Node(value)
            prev_node = self.__get_node(index - 1)
            after_node = prev_node.next
            new_node.prev = prev_node
            new_node.next = after_node
            prev_node.next = new_node
            after_node.prev = new_node
            self.__length += 1
            return True

    def pop(self):
        if self.__length == 0:
            return None

        popped = self.__tail
        if self.__length == 1:
            self.__tail = None
            self.__head = self.__tail
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            popped.prev = None

        self.__length -= 1
        return popped.value

    def pop_first(self):
        if self.__length == 0:
            return None

        popped = self.__head
        if self.__length == 1:
            self.__head = None
            self.__tail = self.__head
        else:
            self.__head = self.__head.next
            self.__head.prev = None
            popped.next = None

        self.__length -= 1
        return popped.value

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.__length - 1:
            return self.pop()
        else:
            prev_node = self.__get_node(index - 1)
            removed_node = prev_node.next
            after_node = removed_node.next
            prev_node.next = after_node
            after_node.prev = prev_node
            removed_node.next = None
            removed_node.prev = None
            self.__length -= 1
            return removed_node.value if removed_node is not None else None

    def __get_node(self, index):
        if index < 0 or index >= self.__length:
            raise Exception('Invalid index of {} specified for Linked List of length {}'.format(index, self.__length))

        if index < self.__length / 2:
            current_node = self.__head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.__tail
            for _ in range(self.__length - 1, index, -1):
                current_node = current_node.prev

        return current_node

    def get_value(self, index):
        return self.__get_node(index).value

    def set_value(self, index, value):
        self.__get_node(index).value = value
        return True

    def print_linked_list(self):
        print('Linked List has {} node{}'.format(self.__length, 's' if self.__length != 1 else ''))
        current_node = self.__head
        idx = 0
        while current_node is not None:
            print('\tNode[{}] value : {}'.format(idx, current_node.value))
            current_node = current_node.next
            idx += 1

    class __Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.print_linked_list()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.insert(0, 'Middle')
    ll.insert(1, 'End')
    ll.prepend('Start')
    ll.insert(2, 'More Middle')
    ll.print_linked_list()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.set_value(0, 'Less Middle')
    ll.print_linked_list()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.print_linked_list()

    ll = DoublyLinkedList(22)
    ll.print_linked_list()

    ll = DoublyLinkedList(11)
    ll.prepend(1)
    ll.append('End')
    ll.print_linked_list()
    print('Removed value {} at index 1'.format(ll.remove(1)))
    print('Removed value {} at index 1'.format(ll.remove(1)))
    ll.print_linked_list()

    ll = DoublyLinkedList('R')
    # Operations that cause exception to be raised
    # ll.insert(2, 'D')
    # ll.insert(-2, 'D')
    ll.insert(1, 'D')
    ll.insert(0, 'F')
    ll.insert(2, 'E')
    ll.print_linked_list()
    print('Node at index: {} has value: {}'.format(0, ll.get_value(0)))
    print('Node at index: {} has value: {}'.format(1, ll.get_value(1)))
    print('Node at index: {} has value: {}'.format(2, ll.get_value(2)))
    print('Node at index: {} has value: {}'.format(3, ll.get_value(3)))
    # print('Node at index: {} has value: {}'.format(4, ll.get_value(4)))

    ll = DoublyLinkedList()
    ll.print_linked_list()
    ll.pop()
    ll.print_linked_list()
    ll.prepend(45)
    ll.print_linked_list()
    ll.pop()
    ll.print_linked_list()
    ll.append(456)
    ll.insert(0, 123)
    ll.print_linked_list()
    ll.pop()
    ll.print_linked_list()
