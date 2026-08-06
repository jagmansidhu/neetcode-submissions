class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = {c: [] for c in range(numCourses)}

        for u, v in prerequisites:
            m[u].append(v)


        visited = set()
        cy = set()
        res = []
        def cycle(cur):
            if cur in cy:
                return False
            if cur in visited:
                return True
            
            cy.add(cur)
            for n in m[cur]:
                if not cycle(n):
                    return False

            cy.remove(cur)
            visited.add(cur)
            res.append(cur)
            return True

        for n in range(numCourses):
            if not cycle(n):
                return []
            

        return res   


