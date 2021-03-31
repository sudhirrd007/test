# 32 ms
# Math


def reverse(self, x: int) -> int:
    
    if(x >= 0):
        ans = int( str(x)[::-1] )
    else:
        ans = -int( str(x)[1:][::-1] )

    if(abs(ans) >= 2**31):
        return 0
        
    return ans