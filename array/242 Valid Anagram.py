class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
            
        count1 = {}
        count2 = {}
        
        for char in s:
            count1[char] = count1.get(char, 0) + 1