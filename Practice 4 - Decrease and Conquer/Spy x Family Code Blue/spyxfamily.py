def minTime_CollectClues(ranks, clue):
    def canCollect_inTime(time):
        total_clues = 0
        for rank in ranks:
            n = 0
            while (rank * (n + 1) ** 2) <= time:
                n += 1
                total_clues += 1
                if total_clues >= clue:
                    return True
        return False
    
    left, right = 0, max(ranks) * (clue ** 2)
    while left < right:
        mid = (left + right) // 2
        if canCollect_inTime(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

ranks = list(map(int, input().split()))
clue = int(input())
print(minTime_CollectClues(ranks, clue))