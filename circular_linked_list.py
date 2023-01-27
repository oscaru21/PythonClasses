# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class CircularLinkedList:
  """list implementation using circularly linked list for storage."""

  #---------------------------------------------------------------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  # end of _Node class
  #---------------------------------------------------------------------------------

  def __init__(self):
    """Create an empty list."""
    self._tail = None                     # will represent tail of list
    self._size = 0                        # number of list elements

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if the list is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the list.

    Raise Empty exception if the list is empty.
    """
    if self.is_empty():
      raise Exception('list is empty')
    head = self._tail._next
    return head._element

  def last(self):
    """Return (but do not remove) the element at the back of the list.
    Raise Empty exception if the list is empty.
    """
    if self.is_empty():
      raise Exception('list is empty')
    return self._tail._element

  def add_first(self, e):
    """Add an element to the back of list."""
    newest = self._Node(e, None)          # node will be new tail node
    if self.is_empty():
      newest._next = newest               # initialize circularly
      self._tail = newest
    else:
      newest._next = self._tail._next     # new node points to head
      self._tail._next = newest           # old tail points to new node
    self._size += 1

  def add_last(self, e):
    """Add an element to the front of list."""
    self.add_first(e)
    self._tail = self._tail._next

  def rotate(self):
    """Rotate front element to the back of the list."""
    if self._size > 0:
      self._tail = self._tail._next       # old head becomes new tail

  def __str__(self):
    """Return a string representation of the list."""
    if self.is_empty():
      return ''

    else:
      current = self._tail
      elements = []
      while True:
        elements.append(str(current._next._element))
        current = current._next
        if current is self._tail:
          break
    return "->".join(elements)