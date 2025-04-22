# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        stack = [0]
        while stack:
            room = stack.pop()
            visited[room] = True
            to_be = rooms[room]
            for i in to_be:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        return all(visited)

