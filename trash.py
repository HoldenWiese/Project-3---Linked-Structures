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