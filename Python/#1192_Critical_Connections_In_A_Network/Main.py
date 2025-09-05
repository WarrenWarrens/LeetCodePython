class Solution(object):
    def tarjan(self, n, c):

        graph = [[] for _ in range(n)]
        for u, v in c:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [-1] * n
        time = [0]
        bridges = []

        def dfs(u, p):
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if v == p:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)
        return bridges

    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.tarjan(n, connections)




