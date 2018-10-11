# Given two integers representing the numerator and denominator
# of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part
#  in parentheses.
#
# Example 1:
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

class Solution:
    def fractionToDecimal(self, x, y):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if x * y < 0 else ''
        x = abs(x)
        y = abs(y)
        head, remain = divmod(x, y)
        tail = ''
        pos = 0
        seen = {}
        while remain != 0:
            if remain in seen:
                return '{}{}.{}({})'.format(sign, head, tail[:seen[remain]], tail[seen[remain] : pos])
            seen[remain] = pos
            digit, remain = divmod(remain * 10, y)
            tail += str(digit)
            pos += 1
        return '%s%s' % (sign, head) if not tail else '%s%s.%s' % (sign, head,tail)