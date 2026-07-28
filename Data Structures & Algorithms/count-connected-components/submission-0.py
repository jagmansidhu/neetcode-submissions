class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()


        def dfs(i):
            visited.add(i)

            for n in adj[i]:
                if n in visited:
                    continue
                dfs(n)


        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count