# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "./":
                continue
            elif stack and log == "../":
                stack.pop()
            elif not stack and log == "../":
                continue
            else:
                stack.append(log)
        return len(stack)
             