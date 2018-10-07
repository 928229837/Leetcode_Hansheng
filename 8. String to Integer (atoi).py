class Solution:
    def myAtoi(self, input):
        """
        :type str: str
        :rtype: int
        """
        MIN_VAL = -2 ** 31
        MAX_VAL = 2 ** 31 - 1

        for i, ch in enumerate(input):
            if ch != ' ':
                break
        else:
            return 0
        # check first char
        ret_val = 0
        sign = -1 if input[i] == '-' else 1
        if input[i] in ('-', '+'): i += 1
        # process the rest
        while i < len(input) and '0' <= input[i] <= '9':
            ret_val = ret_val * 10 + ord(input[i]) - ord('0')
            if ret_val > MAX_VAL:
                break
            i += 1

        if sign > 0:
            return min(MAX_VAL, ret_val)
        else:
            return max(MIN_VAL, -ret_val)