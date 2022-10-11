"My linked list. It's not perfect. It's actually not very good at all, but it works."
class SList:
    "SList is the linked list class"

    class SListNode:
        "Class for creating nodes."

        def __init__(self, value=None):
            "Inner class for nodes."
            self.value = value
            self.next = None
            self.index = None

    def __init__(self):
        "Setting up SList"
        self._head = None
        self._tail = None
        self._prev = None
        self._curr = None
        self._next = None
        self._new_n = None
        self._size = 0

    def insert(self, value):
        "Inserting values in order into list"
        if self._size == 0:
            self._head = self.SListNode(value)
            self._tail = self._head
            self._prev = None
            self._curr = self._head
            self._next = self._curr.next
            self._size = self._size + 1
        else:

            self._curr = self._head
            self._next = self._curr.next

            if value < self._head.value:
                self._new_n = self.SListNode(value)
                self._new_n.next = self._head
                self._head = self._new_n
                self._size = self._size + 1
            else:
                while value >= self._curr.value:
                    self._prev = self._curr
                    self._curr = self._next
                    if self._next is not None:
                        self._next = self._next.next
                    if self._curr is None:
                        break

                self._new_n = self.SListNode(value)
                self._new_n.next = self._curr
                self._prev.next = self._new_n
                self._size = self._size + 1
                if self._new_n.next is None:
                    self._tail = self._new_n

    def find(self, value):
        "Finding values in list"
        if self._head.value is None:
            return None
        else:
            self._curr = self._head
            while self._curr is not None:
                if self._curr.value == value:
                    return self._curr.value
                else:
                    self._curr = self._curr.next
                    if self._next is not None:
                        self._next = self._next.next
        return None

    def remove(self, value):
        "Remove a single value"
        if self._head is not None:
            self._curr = self._head
            self._next = self._curr.next
            if self._curr.value is value:
                self._head = self._next
                self._curr.next = None
                self._size -= 1
                return True
        while self._curr is not None:
            if self._curr.value == value:
                self._prev.next = self._curr.next
                self._curr.next = None
                self._size -= 1
                return True
            self._prev = self._curr
            self._curr = self._next
            if self._next is not None:
                self._next = self._next.next
            if self._curr is None:
                return False

    def remove_all(self, value):
        "Remove all values that match value"
        removed = True
        while removed is True:
            removed = self.remove(value)

    def __str__(self):
        "Stringify the list"
        output = '['

        if self._head is not None:
            self._curr = self._head
            self._next = self._curr.next
        while self._curr is not None:
            if self._next is None:
                output += str(self._curr.value) + ']'
                return output
            output += str(self._curr.value) + ', '
            self._curr = self._next
            if self._next is not None:
                self._next = self._next.next
            if self._curr is None:
                return output

    def __next__(self):
        "Iterator function"
        if self._next is None:
            raise StopIteration

        self._curr = self._next
        self._next = self._next.next
        return self._curr.value

    def __iter__(self):
        "Iterator function"
        self._curr = None
        self._next = self._head
        return self

    def __getitem__(self, key):
        "Use square brackets"
        i = 0
        if self._head is not None:
            self._curr = self._head
            self._next = self._curr.next
        while self._curr is not None:
            self._curr.index = i
            i += 1
            if self._curr.index is key:
                return self._curr.value
            self._curr = self._next
            if self._next is not None:
                self._next = self._next.next
            if self._curr is None:
                break

    def size(self):
        "Return size"
        return self._size

    def __len__(self):
        "Return size"
        return self._size
