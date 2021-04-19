#BFS
#71%
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)

        valid_choices_list = "ACGT"

        queue = collections.deque([start])

        visited = set()
        mutation_count = -1

        while(queue):

            mutation_count += 1

            for i in range(len(queue)):
                cur_mutation = queue.popleft()
                visited.add(cur_mutation)
                if cur_mutation == end:
                    return mutation_count
                for j in range(len(cur_mutation)):
                    for c in valid_choices_list:
                        next_mutation = cur_mutation[:j] + c + cur_mutation[j+1:]
                        if next_mutation in bank and next_mutation not in visited:
                                visited.add(next_mutation)
                                queue.append(next_mutation)

        return -1

#DFS
#71%
#技巧性比较多
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        def dfs(start, end):
            if start in mem:
                return mem[start]
            mem[start] = float('inf')
            for i in range(len(start)):
                for j in ['A', 'C', 'G', 'T']:
                    s = start[:i] + j + start[i + 1:]
                    if s in bank:
                        mem[start] = min(mem[start], dfs(s, end) + 1)
            return mem[start]

        mem = {end: 0}
        bank = set(bank)
        r = dfs(start, end)
        return r if r != float('inf') else -1


#DFS

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            nonlocal min_count

            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    current_bank.add(new)

        dfs(start, 0, bank)

        return min_count if min_count <= len(bank) else -1

