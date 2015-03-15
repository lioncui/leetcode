#There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. 
#The overall run time complexity should be O(log (m+n)).


#!/usr/bin/python
#-*- coding:UTF-8 -*-

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (not A) and (not B):
            return None
        elif A and (not B):
            tmp=list(A)
        elif (not A) and B:
            tmp=list(B)
        else:
            tmp=list(A)
            tmp.extend(B)
        
        tmp.sort()
        print tmp
        i = len(tmp) / 2
        if len(tmp) % 2 == 0:
            return float(tmp[i-1] + tmp[i]) / 2
        else:
            return float(tmp[i])
      
if __name__ == '__main__':  
    a=Solution()
    print a.findMedianSortedArrays([3,4,5], [9,7,6,8])
            