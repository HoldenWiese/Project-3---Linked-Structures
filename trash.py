  def get_head(self):
    if self._head is not None:
      return self._head.value
    else:
      return None

  def get_tail(self):
    if self._tail is not None:
      return self._tail.value
    else:
      return None

  def get_curr(self):
    if self._curr is not None:
      return self._curr.value
    else:
      return None

  def get_next(self):
    if self._next is not None:
      return self._next.value
    else:
      return None


      # while self._curr.value <= value:
      #   print('Current value: ', self._curr.value, ' is less than or equal to ', value)
      #   self._prev = self._curr
      #   self._curr = self._next
      #   if self._next is not None:
      #       self._next = self._next.next
      #   else:
      #     break
      # print('End of while. self._prev: ', self._prev.value, ' self._curr.value:', self._curr)
      # self._newN = self.SListNode(value)
      # self._newN.next = self._curr
      # self._prev.next = self._newN
      # self._size = self._size + 1