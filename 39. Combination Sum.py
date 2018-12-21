class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

    def combina(self, candidates, target, tempList):
        if target == 0:
            return True
        elif target < candidates[0]:
            return False
        for num in candidates:
            self.combina(candidates, target - num, tempList)
            self.combina(candidates[1:], target, tempList)
