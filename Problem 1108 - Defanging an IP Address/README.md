Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.


--------------------------------------------------------------------------------------------------------
Thoughts:

I don't know why someone would need to defang an IP address, and neither does my friend who is a network engineer. Anyway, the address is a string so a replace method or just parsing the string and inserting the brackets should suffice. I've never used these tools in python, so I'll have to research that first