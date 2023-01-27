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

from doubly_linked_base import _DoublyLinkedBase

class DoublyLinkedList(_DoublyLinkedBase):         # note the use of inheritance
  """Double-ended linked list implementation based on a doubly linked list."""

  def first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._header._next._element        # real item just after header

  def last(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._trailer._prev._element       # real item just before trailer

  def add_first(self, e):
    self._insert_between(e, self._header, self._header._next)   # after header

  def add_last(self, e):
    self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

  def delete_first(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._delete_node(self._header._next)   # use inherited method

  def delete_last(self):
    if self.is_empty():
      raise Exception("Deque is empty")
    return self._delete_node(self._trailer._prev)  # use inherited method

  def __str__(self):
    """Return a string representation of the list's elements."""
    current = self._header._next                       # start at the header
    elements = []                                      # elements in the list
    while current is not self._trailer:                # until the trailer is reached
      elements.append(current._element)
      current = current._next
    return '<->'.join(str(elem) for elem in elements)
