# Given a string representing an expression of fraction addition and
# subtraction, you need to return the calculation result in string
# format. The final result should be irreducible fraction. If your
# final result is an integer, say 2, you need to change it to the
# format of fraction that has denominator 1. So in this case, 2
# should be converted to 2/1.
#
# Example 1:
# Input:"-1/2+1/2"
# Output: "0/1"
# Example 2:
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:
# Input:"1/3-1/2"
# Output: "-1/6"
# Example 4:
# Input:"5/3+1/3"
# Output: "2/1"


def Sol_1_fractionAddition(expression):
    """
    :type expression: str
    :rtype: str
    """
    from fractions import Fraction
    res = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))
    return str(res.numerator) + '/' + str(res.denominator)

def sol_2(expression):
    import math
    expression += '+'
    num = 0  # numerator
    buff = ''  # Store number
    t_num = 0  # numerator in total
    t_den = 1  # denominator in total
    attr = 1  # attributes(positive or negative)
    for i in expression:
        if i in {'+', '-'}:
            num_cur, den_cur = num * attr, int(buff if buff else '1')
            t_num = t_num * den_cur + num_cur * t_den
            t_den = t_den * den_cur
            gcd = math.gcd(t_num, t_den)
            t_num, t_den = t_num // gcd, t_den // gcd
            num, buff = '', ''
            attr = -1 if i == '-' else 1
        elif i == '/':
            num, buff = int(buff), ''
        else:
            buff += i
    return str(t_num) + '/' + str(t_den)



a = "-1/2+1/2+1/3"

b = "1/3-1/2"

print(sol_2(a))








