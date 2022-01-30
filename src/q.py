from linked_list import LinkedList


# Had to rename source from queue.py due to problem with Python debugger in IntelliJ:
# - https://intellij-support.jetbrains.com/hc/en-us/community/posts/4405195364114-PyCharm-debugger-isn-t-working
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

    def print(self):
        self.__ll.print()


if __name__ == '__main__':
    q = Queue()
    print(q.length())
    print(q.dequeue())
    q = Queue(56)
    print(q.length())
    print(q.dequeue())
    q.print()
    q.enqueue('Eric')
    q.enqueue('Bob')
    q.enqueue('Nigel')
    q.print()
    print(q.dequeue())
    q.print()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.print()

