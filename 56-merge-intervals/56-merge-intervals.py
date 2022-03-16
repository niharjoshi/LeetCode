class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        merged = []
        
        for interval in intervals:
            
            if merged == []:
                merged.append(interval)
            
            else:
                prev_stop = merged[-1][1]
                curr_start = interval[0]
                curr_stop = interval[1]
                
                if curr_start <= prev_stop:
                    merged[-1][1] = max(prev_stop, curr_stop)
                
                else:
                    merged.append(interval)
        
        return merged
        