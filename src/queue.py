from linked_list import LinkedList


class Queue:
    def __init__(self, initial_value=None):
        self.__ll = LinkedList(initial_value)

    def enqueue(self, value):
        # We add to 'tail' as it is O(1)
        #   - adding to 'head' is also O(1)
        return self.__ll.append(value)

    def dequeue(self):
        # We remove from 'head' as it is O(1)
        #   - removing from 'tail' is a worse option as it is O(n)
        return self.__ll.pop_first()

    def length(self):
        return self.__ll.length

    def print_queue(self):
        self.__ll.print_linked_list()


if __name__ == '__main__':
    q = Queue()
    print(q.length())
    print(q.dequeue())
    q = Queue(56)
    print(q.length())
    print(q.dequeue())
    q.print_queue()
    q.enqueue('Eric')
    q.enqueue('Bob')
    q.enqueue('Nigel')
    q.print_queue()
    print(q.dequeue())
    q.print_queue()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.print_queue()

