class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.combina(candidates, target, [], 0)
        return self.ans

    def combina(self, candidates, target, tempList, index):
        tempListNow = list(tempList)
        if target == 0:
            self.ans.append(tempList)
            return True
        elif index >= len(candidates) or target < candidates[0]:
            return False
        self.combina(candidates, target, tempList, index + 1)
        tempListNow.append(candidates[index])
        self.combina(candidates, target - candidates[index], tempListNow,
                     index)


candidates = [2, 3, 5]
target = 1
sol = Solution()
sol.combinationSum(candidates, target)
print(sol.ans)
