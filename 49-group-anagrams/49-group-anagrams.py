class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = {}
        
        for word in strs:
            
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in ans:
                ans[sorted_word] = [word]
            
            else:
                ans[sorted_word].append(word)
            
        return [word_list for word_list in ans.values()]