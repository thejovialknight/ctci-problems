"""
We are going to implement a class of StringBuilder. A string builder holds a list of strings
which can be added to with an append() method. This makes addition of new strings take O(n) time
instead of O(n^2). The stringbuilder can return a full string using a to_string() method
"""

class StringBuilder:
    string_list = []

    def __init__(self, strings):
        for string in strings:
            self.append(string)

    def append(self, string):
        string_list.append(string)

    def to_string(self)
        return string_list.join()

