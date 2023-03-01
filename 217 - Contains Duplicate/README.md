217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]
Output: true



Example 2:

Input: nums = [1,2,3,4]
Output: false



Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

---------------------------------------------------------------------------------------------------------------------------------------------------

Thoughts:

Seems easy, have a nested for loop and loop through everything. Below is my initial solution. It passed most cases, but it took too long so leetcode couldn't pass one of the problems

def containsDuplicate(self, nums: list[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

So I looked at the solution from herehttps://youtu.be/3OamzN90kPg

Much more efficient