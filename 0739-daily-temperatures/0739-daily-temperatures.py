class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0 for i in range(len(temperatures))]
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, t])
        
        return result