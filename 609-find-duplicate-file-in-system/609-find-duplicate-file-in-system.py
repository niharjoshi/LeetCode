class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        index = {}
        
        res = []
        
        for path in paths:
            
            prefix, *contents = path.split(" ")
            
            for file in contents:
                
                file_s = file.split("(")
                file_name = file_s[0]
                file_data = "(" + file_s[1]
                
                if file_data not in index:
                    index[file_data] = [prefix + "/" + file_name]
                else:
                    index[file_data].append(prefix + "/" + file_name)
            
        for k, v in index.items():
            if len(v) > 1:
                res.append(index[k])
        
        return res
        