def containsDuplicate(self, nums: list[int]) -> bool:
    #from https://youtu.be/3OamzN90kPg

    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False