class SList:

  class SListNode:
    def __init__(self, value=None):
      self.value = value
      self.next = None
      self.index = None

  def __init__(self):
    self._head = None
    self._tail = None
    self._prev = None
    self._curr = None
    self._next = None
    self._newN = None
    self._size = 0

  '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
  def insert(self, value):
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
        self._newN = self.SListNode(value)
        self._newN.next = self._head
        self._head = self._newN
        self._size = self._size + 1
      else:
        while value >= self._curr.value:
          self._prev = self._curr
          self._curr = self._next
          if self._next is not None:
            self._next = self._next.next
          if self._curr is None:
            break

        self._newN = self.SListNode(value)
        self._newN.next = self._curr
        self._prev.next = self._newN
        self._size = self._size + 1
        if self._newN.next is None:
          self._tail = self._newN

  '''Search for a value in the list, return it if found, None otherwise'''
  def find(self, value):
    if (self._head.value == None):
      return None
    else:
      self._curr = self._head
      while self._curr is not None:
        if (self._curr.value == value):
          return value
        else:
          self._curr = self._curr.next
          if self._next is not None:
            self._next = self._next.next
    return None

  '''Remove the first occurance of value.'''

  def remove(self, value):
    if self._head is not None:
      self._curr = self._head
      self._next = self._curr.next
      if self._curr.value is value:
        self._head = self._next
        self._curr.next = None
        self._size -= 1
        return True
    while self._curr is not None:
      if self._curr.value is value:
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

  '''Remove all instances of value'''

  def remove_all(self, value):
    removed = True
    while removed is True:
      removed = self.remove(value)

  '''Convert the list to a string and return it'''

  def __str__(self):
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
    if self._next is None:
      raise StopIteration

    self._curr = self._next
    self._next = self._next.next
    return self._curr.value

  '''Return an iterator for the list'''

  def __iter__(self):
    self._curr = None
    self._next = self._head
    return self

  '''Return the item at the given index, or throw an exception if invalid index'''

  def __getitem__(self, key):
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
    return self._size

  def __len__(self):
    return self._size
