class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
    
        char = {}
        for i in range(n):
            key = tuple(sorted(words[i]))
            if key in char.keys():
                char[key].append(words[i])
            else:
                char.update({key: [words[i]]})
        
        return char.values()
            
        
        #code here
        
obj = Solution()
obj.Anagrams(['act','god','cat','dog','tac'],5)
