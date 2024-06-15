'''
	Given two binary strings, return their sum (also a binary string).

	The input strings are both non-empty and contains only characters 1 or 0.

	Example 1:

	Input: a = "11", b = "1"
	Output: "100"

	Example 2:

	Input: a = "1010", b = "1011"
	Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        result = ""
        carry = 0
        index_a, index_b = len(a) - 1, len(b) - 1
        
        while index_a >= 0 or index_b >= 0 or carry:
            sum_val = carry
            if index_a >= 0:
                sum_val += int(a[index_a])
                index_a -= 1
            if index_b >= 0:
                sum_val += int(b[index_b])
                index_b -= 1
            
            result = str(sum_val % 2) + result
            carry = sum_val // 2
        
        if carry > 0:
            result = str(carry) + result
        
        return result

# Example usage:
# sol = Solution()
# print(sol.addBinary("11", "1"))    # Output: "100"
# print(sol.addBinary("1010", "1011"))  # Output: "10101"
