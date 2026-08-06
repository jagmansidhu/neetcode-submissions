class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            m[u].append(v)

        visited = set()

        def check(cur):
            if cur in visited:
                return False

            if m[cur] == []:
                return True

            visited.add(cur)
            for e in m[cur]:
                if not check(e):
                    return False
            visited.remove(cur)
            m[cur] = []
            return True


        for e in range(numCourses):
            if not check(e):
                return False
 
        return True