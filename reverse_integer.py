class Solution:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example : 1
        Input: 123
        Output: 321

    Example : 2
        Input: -123
        Output: -321

    Example : 3
        Input: 120
        Output: 21
    """
    def __init__(self):
        self.orig_int = None
        self.orig_int_digits = []

    def reverse(self, x):
        """
        :type x: int
        :rtype: int (reverse digits of an 32-bit signed integer.)
        """
        if x < 0:
            print('do something')
            return -self.reverse(-x)

        result = 0
        while x:
            result = (result * 10) + (x % 10)
            # print('result : ', result)
            x = int(x / 10)

        if result > (2 ** 31)-1 or result < -(2 ** 31):
            # 32-bit signed integer range: [-2^31, (2^31)-1]
            # Assume that your function returns 0 when the reversed integer overflows.
            return 0
        return result

orig_int = 123
print(Solution().reverse(orig_int))
orig_int = 321
print(Solution().reverse(orig_int))
orig_int = -123
print(Solution().reverse(orig_int))
orig_int = -321
print(Solution().reverse(orig_int))
orig_int = 120
print(Solution().reverse(orig_int))
orig_int = 1
print(Solution().reverse(orig_int))
orig_int = 10
print(Solution().reverse(orig_int))
orig_int = 0
print(Solution().reverse(orig_int))
orig_int = 100000
print(Solution().reverse(orig_int))
orig_int = 1534236469
print(Solution().reverse(orig_int))