"""
Complexity Analysis
-------------------
Time:  O(N+E)
Space: O(N)
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = set({0})

        def dfs(r):
            for k in rooms[r]:
                if k not in seen:
                    seen.add(k), dfs(k)

        dfs(0)
        
        return len(seen) == len(rooms)