

Problem:

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
-----------------------------------------------------------------------------------------------------------------------------

Thoughts:
I've seen this problem before, but haven't solved it. The examples here are deceiving, because if n = 4, there are 5 
unique ways. If n = 5, the answer jumps to 8 (with quick napkin math). There might be a fancy equation to determine this,
but alas I haven't done that kind of math in nearly a decade. It seems like a recursive function would work here, but 
I'd need to investigate first. To the internet!

Yes a recursive function is possible, but quite slow. Weirdly enough, apparently a for loop is better. Seems like the 
inverse is true with these kinds of problems