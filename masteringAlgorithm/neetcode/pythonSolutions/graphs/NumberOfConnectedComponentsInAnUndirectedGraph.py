from typing import List


class Solution:
    def countComponentsUnionFind(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        result = n

        for e1, e2 in edges:
            result -= union(e1, e2)

        return result

    def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:
        return  0