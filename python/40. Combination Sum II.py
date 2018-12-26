# NOTE:延续39题的思路
# NOTE:Runtime: 748 ms, faster than 7.36% of Python3 online submissions for Combination Sum II.
# TODO: solution


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates, target):
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
            if tempListNow not in self.ans:
                self.ans.append(tempList)
            return True
        elif index >= len(candidates) or target < candidates[0]:
            return False
        self.combina(candidates, target, tempList, index + 1)
        tempListNow.append(candidates[index])
        # 不管有没有加入列表，index都加1
        self.combina(candidates, target - candidates[index], tempListNow,
                     index + 1)


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
sol = Solution()
sol.combinationSum2(candidates, target)
print(sol.ans)
