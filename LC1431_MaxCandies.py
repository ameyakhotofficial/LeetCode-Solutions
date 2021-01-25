class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        high = max(candies)
        for x in candies:
            if x+extraCandies>=high:
                ans.append(True)
            else: 
                ans.append(False)
        return ans