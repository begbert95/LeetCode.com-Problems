def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = [None] * (2 * n)
        
        
        for i in range(0, n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[i + n]
        
        return ans