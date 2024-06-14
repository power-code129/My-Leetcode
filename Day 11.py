#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Example 1:
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.

#Example 2:
#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

#Constraints:
#1 <= haystack.length, needle.length <= 104
#haystack and needle consist of only lowercase English characters
  
#program 

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Check if needle is an empty string
        if not needle:
            return 0
        
        # Get the lengths of haystack and needle
        len_haystack, len_needle = len(haystack), len(needle)
        
        # Loop through the haystack
        for i in range(len_haystack - len_needle + 1):
            # Check if the substring matches the needle
            if haystack[i:i+len_needle] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1
