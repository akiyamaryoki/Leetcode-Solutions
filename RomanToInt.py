class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        minus = False
        i = len(s) - 1
        result = 0
        while i >= 0:
            if s[i] == 'I':
                if minus:
                    result -= 1
                    minus = False
                else:
                    result += 1
            elif s[i] == 'V':
                if s[i - 1] == 'I':
                    minus = True
                result += 5
            elif s[i] == 'X':
                if minus:
                    result -= 10
                    minus = False
                else:
                    if s[i - 1] == 'I':
                        minus = True
                    result += 10
            elif s[i] == 'L':
                if s[i - 1] == 'X':
                    minus = True
                result += 50
            elif s[i] == 'C':
                if minus:
                    result -= 100
                    minus = False
                else:
                    if s[i - 1] == 'X':
                        minus = True
                    result += 100
            elif s[i] == 'D':
                if s[i - 1] == 'C':
                    minus = True
                result += 500
            elif s[i] == 'M':
                if s[i - 1] == 'C':
                    minus = True
                result += 1000
            i -= 1
        return result

 