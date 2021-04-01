"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    all = list(range(left, right+1))
    final = []
    for i in all:
        if(i%10 != 0):
            final.append(i)

    ans = []

    def calculate(num):
        numbers = list(str(num))
        if("0" in numbers):
            return False
        for i in numbers:
            if(num%int(i) != 0):
                return False
        return True

    l = [1,2,3,4,5,6,7,8,9]
    for i in final:
        if(i in l):
            ans.append(i)
        elif(calculate(i)):
            ans.append(i)
    return ans