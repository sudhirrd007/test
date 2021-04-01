# 104 ms
# Array, Binary Search, Divide And Conquer

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    arr = sorted((nums1 + nums2))
    length = arr.__len__() - 1

    ans = float(( arr[int(length/2)] + arr[int((length+1)/2)] ) / 2)

    return ans