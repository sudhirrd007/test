# File, 0007_reverse_integer.py
# #, 7
# Title, Reverse Integer
# Run Time, 32 ms
# Difficulty, EASY
# Acceptance rate, 25.9%
# LeetCode Link, https://leetcode.com/problems/reverse-integer/
# Topics, Math


def reverse(self, x: int) -> int:
    
    if(x >= 0):
        ans = int( str(x)[::-1] )
    else:
        ans = -int( str(x)[1:][::-1] )

    if(abs(ans) >= 2**31):
        return 0
        
    return ans