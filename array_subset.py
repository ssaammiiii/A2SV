#User function Template for python3

from collections import Counter 
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freqa = Counter(a)
        freqb = Counter(b)
        for key, value in freqb.items():
            if key in freqa:
                if value > freqa[key]:
                    return False
            else:
                return False
        return True
                    
