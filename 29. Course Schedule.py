class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for x, y in prerequisites:
            outdegree[y].add(x)
            indegree[x].add(y)
        ctr = 0
        in_zero = []
        for i in range(numCourses):
            if not indegree[i]:
                in_zero.append(i)
                ctr += 1
        while in_zero:
            node = in_zero.pop()
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    in_zero.append(x)
                    ctr += 1
        return ctr == numCourses
                
