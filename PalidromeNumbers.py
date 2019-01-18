class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        length = len(x_str)
        midpoint = length // 2
        for i in range(0, midpoint+1):
            if x_str[i] != x_str[length-i-1]:
                return False
        return True