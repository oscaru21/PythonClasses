
class SinglyLinkedList:

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    """Create an empty stack."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def add_first(self, e):
    """Add element e to the head of the list."""
    self._head = self._Node(e, self._head)  # create and link a new node
    self._size += 1

  def first(self):
    """Return (but do not remove) the element at the head of the list.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def remove_first(self):
    """Remove and return the head
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    answer = self._head._element
    self._head = self._head._next           # bypass the former top node
    self._size -= 1
    return answer
  
  def __str__(self):
    """Return a string representation of the list's elements."""
    current = self._head                               # start at the head
    elements = []                                      # elements in the list
    while True:                # until the trailer is reached
      elements.append(current._element)
      if current._next is not None:
        break
      current = current._next
    return '->'.join(str(elem) for elem in elements)

    