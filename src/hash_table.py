from linked_list import LinkedList


class HashTable:
    # To decrease likelihood of collisions we default to a prime number
    table_size = 7

    def __init__(self, initial_size=None):
        size = initial_size if initial_size is not None else HashTable.table_size
        self.__table = [None] * size

    def __hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) * 43
        return hash % len(self.__table)

    def put(self, key, value):
        entry = {key: value}
        idx = self.__hash(key)
        if self.__table[idx] is None:
            self.__table[idx] = LinkedList(entry)
        else:
            ll = self.__table[idx]
            for i in range(ll.length):
                single_entry_dict = ll.get_value(i)
                # Test for whether the key of single entry dictionary matches
                try:
                    single_entry_dict[key]
                    ll.set_value(i, entry)
                    break
                except KeyError:
                    pass
            else:
                # Weren't able to find a matching key, so add it
                ll.append(entry)

    def get(self, key):
        idx = self.__hash(key)
        if self.__table[idx] is not None:
            ll = self.__table[idx]
            for i in range(ll.length):
                single_entry_dict = ll.get_value(i)
                # Test for whether the key of single entry dictionary matches
                try:
                    value = single_entry_dict[key]
                    return value
                except KeyError:
                    pass

            # No linked list or unable to find a matching key
            return None

    def keys(self):
        keys = []
        for idx in range(len(self.__table)):
            if self.__table[idx] is not None:
                ll = self.__table[idx]
                for i in range(ll.length):
                    single_entry_dict = ll.get_value(i)
                    keys.append(next(iter(single_entry_dict.keys())))

        return keys

    def print_table(self):
        print()
        for i, j in enumerate(self.__table):
            contents = None if j is None else j.ll_as_string()
            print("Bucket[{}] : {}".format(i, contents))


if __name__ == "__main__":
    ht = HashTable()
    ht.print_table()
    ht.put("egg", 2)
    ht.print_table()
    ht.put("apple", 11)
    ht.print_table()
    ht.put("lemon", 4)
    ht.print_table()
    ht.put("tomato", 23)
    ht.print_table()
    ht.put("grape", 16)
    ht.print_table()
    print("We have {} grapes".format(ht.get("grape")))
    ht.put("grape", 33)
    ht.print_table()
    print("We have {} dinosaurs".format(ht.get("dinosaur")))
    print(ht.keys())
