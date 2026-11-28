class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g=defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        unvisited=0
        visiting=1
        visited=2
        states=[unvisited]*numCourses
        path=[]
        def dfs(node):
            state=states[node]
            if state==visited:
                return True
            elif state==visiting:
                return False
            states[node]=visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node]=visited
            path.append(node)
            return True          
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path