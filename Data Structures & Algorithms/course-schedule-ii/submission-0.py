from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and track in-degrees
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Queue all courses with 0 in-degree (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        # Process courses in topological order
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Return order if all courses can be taken, else empty list (cycle detected)
        return order if len(order) == numCourses else []