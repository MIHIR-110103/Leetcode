class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_len = len(min(strs, key=len))
        
        let = 0
        while let < min_len:
            for wod in strs:
                if wod[let] != strs[0][let]:
                    return strs[0][:let]
            let += 1
        
        return strs[0][:min_len]


        
