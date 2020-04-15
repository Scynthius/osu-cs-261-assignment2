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

    def get_array(self):
        return self._list[:self._size]

    def append(self, val):
        """
        Inserts a new element in self._list or calls the expand function to create space if the list is full.
        """
        if self._capacity == self._size:
            self._expand()
        self._list[self._size:] = val
        self._size += 1

    def pop(self):
        """
        Removes the last element of the list and returns it to the caller.
        """
        popped = self._list[self._size - 1]
        self._size -= 1
        return popped

    def insert(self, index, val):
        """
        Inserts the val parameter at the given index. If index goes beyond the final list element, the function acts as
        an append. Utilizes the private expand function if the array cannot fit the new entry.
        """
        if index < self._size and self._size + 1 <= self._capacity:
            # Index is within existing array and there is available capacity. Shift elements and insert val.
            temp = self._size
            while temp > index:
                self._list[temp] = self._list[temp - 1]
                temp -= 1
            self._list[index] = val
            self._size += 1
        elif self._size + 1 <= self._capacity:
            self._list[self._size:] = val
            self._size += 1
        else:
            self._expand()
            self.insert(index, val)

    def remove(self, val):
        """
        Removes all instances of the parameter value from the array and condenses the list as necessary.
        """
        if val in self._list:
            counter = 0
            for i in range(0, self._size):
                if self._list[i] == val:
                    for x in range(i, self._size - 1 - counter):
                        self._list[x] = self._list[x + 1]
                    self._list[self._size - 1] = 0
                    counter += 1
            self._size -= counter

    def clear(self):
        new_arr = np.empty(self._capacity, np.int16)
        self._list = new_arr
        self._size = 0

    def count(self, val):
        total = 0
        for i in range(self._size - 1):
            if self._list[i] == val:
                total += 1
        return total

    def get(self, index):
        if index <= self._size:
            return self._list[index]

    def _expand(self):
        """
        Doubles the size of self._list and updates self._capacity accordingly.
        """
        new_arr = np.empty(self._capacity * 2, np.int16)
        for i in range(self._capacity):
            new_arr[i] = self._list[i]
        self._capacity *= 2
        self._list = new_arr

#Testing
test1 = StudentList()
test1.append(15)
print(test1.get_array())
test1.append(12)
test1.append(18)
test1.append(50)
test1.insert(2, 20)
print(test1.get_array())
test1.append(100)
print(test1.get_list())
print(test1.pop())
print(test1.get_list())
test1.append(20)
print(test1.get_list())
test1.insert(2, 123)
print(test1.get_list())
test1.append(12)
print(test1.get_list())
test1.remove(12)
print(test1.get_list())
print(test1.get(2))
test1.clear()
print(test1.get_list())