class Solution(object):
    def minCostConnectPoints(self, points):
        n=len(points)
        visited=set()
        heap=[(0,0)]
        total=0

        while len(visited)<n:
            cost,i=heapq.heappop(heap)

            if i in visited:
                continue

            visited.add(i)
            total += cost

            for j in range(n):
                if j not in visited:
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    dist=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,(dist,j))

        return total


       