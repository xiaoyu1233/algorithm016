class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        endList = [0] * 26
        for i, ch in enumerate(S):
            endList[ord(ch) - ord("a")] = i

        res = []
        left = most_right = 0
        for i, ch in enumerate(S):
            most_right = max(most_right, endList[ord(ch) - ord("a")])
            if i == most_right:
                res.append(most_right - left + 1)
                left = most_right + 1
        return res
