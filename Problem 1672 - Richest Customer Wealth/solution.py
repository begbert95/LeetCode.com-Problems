
def maximumWealth(accounts: list[list[int]]) -> int:

    highestWealth = 0
    for i in range(len(accounts)):
        total = 0
        
        for j in range(len(accounts[i])):
            total += accounts[i][j]
        
        if total > highestWealth:
            highestWealth = total
    return highestWealth


accounts = [[2,8,7],[7,1,3],[1,9,5]]

print(maximumWealth(accounts))