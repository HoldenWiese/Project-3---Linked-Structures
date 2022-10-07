
class SList:
  class SListNode:
    def __init__ (self, value = None):
      self.value = value
      self.next = None

  def __init__ (self):
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
      self._next = self._head.next
      self._size = self._size + 1
    else:
      while value > self._curr:
        self._prev = self._curr
        self._curr = self._next
        if self._next is not None:
            print(self._next)
            self._next = self._next.next
      self._newN = self.SListNode(value)
      self._newN.next = self._curr
      self._prev.next = self._newN
        
    
  '''Search for a value in the list, return it if found, None otherwise'''
  def find(self, value):
    found = False

    if(self._head.value == None):
      return None
    else:
      while self._curr is not None:
        if(self._curr.value == value):
          return value
        else:
          self._curr = self._next
          if self._next is not None:
            print(self._next)
            self._next = self._next.next
          else:
            found = False
    return None

  '''Remove the first occurance of value.'''
  def remove(self, value):
    pass

  '''Remove all instances of value'''
  def remove_all(self, value):
    pass

  '''Convert the list to a string and return it'''
  def __str__(self):
    pass

  '''Return an iterator for the list'''
  def __iter__(self):
    pass

  '''Return the item at the given index, or throw an exception if invalid index'''
  def __getitem__(self, index):
    pass

  def __len__(self):
    pass
  

  