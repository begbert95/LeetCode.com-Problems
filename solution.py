def runningSum(self, nums: List[int]) -> List[int]:
        sums = []

        for i in nums:
            if(len(sums) == 0):
                sums.append(i)
            else:
                sums.append(sums[-1] + i)
        return sums