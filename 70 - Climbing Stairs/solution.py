class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 3):
            return n

        arr = [0] * (n + 1)

        for i in range(4):
            arr[i] = i

        for i in range(4, n + 1):
            print(i)
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[n]
