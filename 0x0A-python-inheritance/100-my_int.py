#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 12 """


class MyInt(int):
      def __eq__(self, other):
          return int(self) != int(other)

    def __ne__(self, other):
       
        return int(self) == int(other)
