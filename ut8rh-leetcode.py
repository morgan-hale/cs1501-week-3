# Umika Tunuguntla (ut8rh)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        arr= []
        
        arr= (s.strip()).split(" ")
        index = len(arr) - 1
        return len(arr[index])
        