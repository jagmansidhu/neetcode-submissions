class Solution:
    '''
        Use adj list to type in all the edges of each node
        Using BFS or DFS we loop through the list and add all connected nodes to visited
        If the nodes are not connected to same graph we will count += 1 
        because we are doing another search. 
        If all in same graph we will do only one bfs in our outer for loop with dfs(i)
    '''
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