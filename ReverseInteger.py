class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_1 = x
        if x < 0:
            x = abs(x)
        digits = len(str(x))
        ans = 0
        curr = digits
        while curr != 0:
            new = x // (10 ** (curr - 1))
            ans += new * (10 ** (digits - curr))
            x -= new * (10 ** (curr - 1))
            curr -= 1
        if ans < 0 - 2 ** 31 or ans > 2 ** 31 - 1:
            return 0
        elif x_1 < 0:
            return 0 - ans
        else:
            return ans