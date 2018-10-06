class Solution:

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        array = []
        for num in ops:
            if num == 'C':
                array = array[:-1]
            elif num == 'D':
                array.append(int(array[-1]) * 2)
            elif num == '+':
                array.append(int(array[-1]) + int(array[-2]))
            else:
                array.append(int(num))

            print(num, array)
        return sum(array)


test = Solution()
print(test.calPoints(["-21","-66","39","+","+"]))


