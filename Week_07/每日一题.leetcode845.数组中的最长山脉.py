class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l1, l2 = len(name), len(typed)
        i, j = 0, 0
        while j < l2:
            if i < l1 and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == l1