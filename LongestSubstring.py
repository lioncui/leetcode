#Given a string, find the length of the longest substring without repeating characters. 
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
#For "bbbbb" the longest substring is "b", with the length of 1


#!/usr/bin/python
#-*- coding:UTF-8 -*-

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        length=0
        index=1
        count=len(s)
        if count == 1:
            return 1
        elif count ==2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        else:
            for i in range(count-1):
                #index=i+length
                action=True
                while action:
                    if s[index] in s[i:index]:
                        exist=0
                        action=False
                    if (action == True) and (index != count-1):
                        index+=1
                    elif action == True:
                        exist=1
                        action=False
                if len(s[i:index+exist]) > length:
                    length=len(s[i:index+exist])
                    print s[i:index+exist]
            return length
a=Solution()
print a.lengthOfLongestSubstring('lionstudypython')

