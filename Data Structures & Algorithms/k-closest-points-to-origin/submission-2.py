class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for xy in points:
            dis = xy[0]**2 + xy[1]**2
            distance.append(dis)

        for i in range (1, len(points)):
            j = i
            while j>0 and distance[j-1] > distance[j]:
                distance[j], distance[j-1] = distance[j-1], distance[j]
                points[j], points[j-1] = points[j-1], points[j]
                j -= 1
        
        print(distance)
        print(points) 

        l1 = []

        for i in range(0,k):
            l1.append(points[i])

        return l1