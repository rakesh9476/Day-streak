import sys
class Solution:
    sys.set_int_max_str_digits(100000)
    def findSum(self, s1, s2):
        b=int(s1)+int(s2)
        return str(b)
