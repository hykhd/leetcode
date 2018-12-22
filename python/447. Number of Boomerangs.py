import math
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dis = set()
        for i in range(len(points)):
            for j in range(i,len(points)):
                dis[self.distance(points[i],points[j])] += 1
    def distance(self,p1,p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2