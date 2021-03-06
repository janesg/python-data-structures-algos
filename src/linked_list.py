class LinkedList:
    def __init__(self, initial_value=None):
        self.__head = None
        self.__length = 0

        if initial_value is not None:
            self.__head = LinkedList.__Node(initial_value)
            self.__length = 1

        self.__tail = self.__head

    @property
    def length(self):
        return self.__length

    def append(self, value):
        new_node = LinkedList.__Node(value)
        if self.__length == 0:
            self.__tail = new_node
            self.__head = self.__tail
        else:
            self.__tail.next = new_node
            self.__tail = self.__tail.next

        self.__length += 1
        return True

    def prepend(self, value):
        new_node = LinkedList.__Node(value)
        if self.__length == 0:
            self.__head = new_node
            self.__tail = self.__head
        else:
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
            new_node = LinkedList.__Node(value)
            prev_node = self.__get_node(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
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
            self.__tail = self.__get_node(self.__length - 2)
            self.__tail.next = None

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
            prev_node.next = removed_node.next
            removed_node.next = None
            self.__length -= 1
            return removed_node.value

    def reverse(self):
        if self.__length >= 2:
            temp = self.__head
            self.__head = self.__tail
            self.__tail = temp

            before = None
            for _ in range(self.__length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after

    def __get_node(self, index):
        if index < 0 or index >= self.__length:
            raise Exception('Invalid index of {} specified for Linked List of length {}'.format(index, self.__length))

        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def get_value(self, index):
        return self.__get_node(index).value

    def set_value(self, index, value):
        self.__get_node(index).value = value
        return True

    def contains(self, value):
        current_node = self.__head
        for _ in range(self.__length):
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def print(self):
        print('Linked List has {} node{}'.format(self.__length, 's' if self.__length != 1 else ''))
        current_node = self.__head
        idx = 0
        while current_node is not None:
            print('\tNode[{}] value : {}'.format(idx, current_node.value))
            current_node = current_node.next
            idx += 1

    def as_string(self):
        return_str = ""
        current_node = self.__head
        idx = 0
        while current_node is not None:
            if len(return_str) == 0:
                return_str = str(current_node.value)
            else:
                return_str = return_str + ', ' + str(current_node.value)

            current_node = current_node.next
            idx += 1

        return return_str

    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.insert(0, 'Middle')
    ll.insert(1, 'End')
    ll.prepend('Start')
    ll.insert(2, 'More Middle')
    ll.print()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.set_value(0, 'Less Middle')
    ll.print()
    print('Popped node value: {}'.format(ll.pop()))
    print('Pop first node value: {}'.format(ll.pop_first()))
    ll.print()

    ll = LinkedList(22)
    ll.print()

    ll = LinkedList(11)
    ll.prepend(1)
    ll.append('End')
    ll.print()
    ll.reverse()
    ll.print()
    print('Removed value {} at index 1'.format(ll.remove(1)))
    print('Removed value {} at index 1'.format(ll.remove(1)))
    ll.reverse()
    print('Removed value {} at index 0'.format(ll.remove(0)))
    ll.reverse()
    print('Removed value {} at index 0'.format(ll.remove(0)))
    ll.print()

    ll = LinkedList('R')
    # Operations that cause exception to be raised
    # ll.insert(2, 'D')
    # ll.insert(-2, 'D')
    ll.insert(1, 'D')
    ll.insert(0, 'F')
    ll.insert(2, 'E')
    ll.print()
    for i in range(4):
        print('Node at index: {} has value: {}'.format(i, ll.get_value(i)))

    ll = LinkedList()
    ll.print()
    ll.pop()
    ll.print()
    ll.prepend(45)
    ll.print()
    ll.pop()
    ll.print()
    ll.append(456)
    ll.insert(0, 123)
    ll.print()
    print("Contains 456 : {}".format(ll.contains(456)))
    print("Contains 666 : {}".format(ll.contains(666)))
    ll.pop()
    ll.print()
