def isPalindrome(self, s: str) -> bool:
    newS = ""
    for c in s.lower():
        if c.isalnum():
            newS += c
    return newS == newS[::-1]