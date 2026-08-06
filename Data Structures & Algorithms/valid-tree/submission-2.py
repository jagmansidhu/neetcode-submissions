class Solution:

    '''
        A tree is valid when no circular dependencies and one connected graph
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {c: [] for c in range(n)}

        for u, v in edges:
            m[u].append(v)
            m[v].append(u)

        visited = set()

        def check(cur, par):
            if cur in visited:
                return False

            visited.add(cur)
            for n in m[cur]:
                if n == par:
                    continue
                if not check(n, cur):
                    return False
            
            return True
        
        count = 0
        for i in range(n):
            if i in visited:
                continue
            if not check(i, -1):
                return False

            count += 1
            # if count > 1:
            #     return False

        return True if count <= 1 else False








        