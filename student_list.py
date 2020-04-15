# student_list.py
# ===================================================
# Reimplementation of Pythons List
# Author: Jonathan Fryman
# Date: 4/14/2020
# ===================================================

import numpy as np


class StudentList:
    def __init__(self):
        """
        Creates a new StudentList object as an array with a capacity of 4 16-bit integers. Initializes the capacity and
        size private attributes to 4 and 0, respectively.
        """
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        """
        Converts self to string for debugging. Displays the array elements.
        """
        return str(self._list[:self._size])

    def get_list(self):
        return self._list[:self._size]


	def get_capacity(self):
        return self._capacity

	def append(self, val):
        """
        Inserts a new element in self._list or calls the expand function to create space if the list is full.
        """
		if self._capacity == self._size:
            _expand()
        self._list[self._size:] = val
        self._size += 1

	def pop(self):
		popped = self._list[self._size - 1]
        self._list[self._size - 1] = None
        return popped


	def insert(self, index, val):
        None

	def remove(self, val):
		None

	def clear(self):
        None
	def count(self):
		None

	def get(self, index):
		None

    def _expand(self):
        """
        Doubles the size of self._list and updates self._capacity accordingly.
        """
        new_arr = np.empty(self._capacity * 2, np.int16)
        for i in range(self._capacity):
            new_arr[i] = self._list[i]
        self._capacity *= 2
        self._list = new_arr
