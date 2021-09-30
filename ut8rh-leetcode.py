# Umika Tunuguntla (ut8rh)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        vals = " "

        for x in digits:
            vals += str(x)
        int1 = int(vals) 
        final = str(int1+1)
        
        
        lastA=[int(x) for x in final]
        
        
        return lastA
        