#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""

#Explanation: There is no common prefix among the input strings.
 

#Constraints:
#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def prefix(strs, index):
            check_prefix = strs[0][:index]
            for index in range(1, len(strs)):
                if not strs[index].startswith(check_prefix):
                    return False
            return True
                
                    
        if not strs:
            return ""
        
        minLength = float('inf')
        for string in strs:
            minLength = min(minLength, len(string))
            
        low, high = 0, minLength
        
        while low <= high:
            mid = (low+high)/2
            if (prefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1
        
        return strs[0][:(low+high)/2]