class Solution:
    def ispar(self,x):
        pair = {'}':'{',']':'[',')':'('}
        arr = []
        if len(x)%2:
            return False
        for char in x:
            if char in ['[','(','{']:
                arr.append(char)
                
            if char in [']',')','}']:
                if not arr:
                    return False
                if pair[char] != arr.pop():
                    return False
        if arr:
            return False
        return True
                
obj = Solution()
obj.ispar("{{{}}")
