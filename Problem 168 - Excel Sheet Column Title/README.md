Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"



Example 2:

Input: columnNumber = 28
Output: "AB"



Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 2^(31) - 1

---------------------------------------------------------------------------------------------------------------

Thoughts: 

Seems like there are two things that need to happen. First, make a dictionary with A = 1 through Z = 26. As far as I know, python doesn't have a way to iterate through the alphabet, so it would need to be done manually Second, find an equation that can convert it. Definitely tough until you figure out the equation.

I knew a few things:
    1. You'll need to use a while loop or iterable function
    2. You'll need to use % 26 somewhere in the loop
    3. You'll need to map it to the alphabet

I tried a few variations, but the problem was with my dictionary. I couldn't find the right setup to allow me to get what I wanted. Luckily I found a solution that worked. I think an array of strings would've worked better, but I thought of that only after I found the solution. Seems like the biggest hurdle for me was just not knowing the ord and chr functions

solution provided here by PratikSen07 https://leetcode.com/problems/excel-sheet-column-title/solutions/2448578/easy-0-ms-100-fully-explained-java-c-python-python3/