242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---------------------------------------------------------------------------------------------------------------------------------

Thoughts: 

Seems like you would parse through the string s and turn it into a character list, then loop through t and remove each character from the s list. I don't know the python string manipulation off the top of my head, so a little research is required. For the follow up, I think you'd convert everything to it's numeric value, aka 'A' = 65