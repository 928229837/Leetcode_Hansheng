import re


class Solution(object):
    def myAtoi(self, str):
        if not str:
            return 0
        str = str.strip()
        out = re.search(r"[+-]?\d+", str)
        if out:
            s = out.start()
            e = out.end()
            if re.search(r"[\D]+", str[:s]):
                return 0
            i = int(str[s:e])
            if i > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if i < -2 ** 31:
                return -2 ** 31

            return i
        return 0