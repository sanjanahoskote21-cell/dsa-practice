class Solution(object):
    def rh(self,x, rev):
        if x == 0:
            return rev
        return self.rh(x // 10, rev * 10 + x % 10)

    def reverse(self, x):
        sign = -1 if x < 0 else 1
        rev = self.rh(abs(x), 0)
        
        return sign * rev if rev <= 2**31 - 1 else 0

        """
        :type x: int
        :rtype: int
        """
        