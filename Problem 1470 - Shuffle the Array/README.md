Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
 

Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

------------------------------------------------------------------------------------------------------------------------
Thoughts:

This is somewhat complicated. I tried doing it on my own, but couldn't get the complete answer. I got part of the array correct, but the second half was wrong. I looked at the solution provided by rahulvarma5297 https://leetcode.com/problems/shuffle-the-array/solutions/3148841/easy-solution-c-java-python-100-faster-beginner-friendly-best-method/, and realized I was misreading the problem, thinking that it was saying nums length was 2*len(nums) after the iteration, and that didn't make any sense to me (obviously)