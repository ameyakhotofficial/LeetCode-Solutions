class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        c = 0 
        
        for x in nums:
            c += x
            answer.append(c)
        return answer