from collections import defaultdict
#BFS

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_node_dict = defaultdict(list)
        blue_node_dict = defaultdict(list)

        for edge in red_edges:
            red_node_dict[edge[0]].append(edge[1])

        for edge in blue_edges:
            blue_node_dict[edge[0]].append(edge[1])

        # 其实阶段有两种可能性，一种是先选择红色开始，一种是先选择蓝色开始, 最后两种取最短的路径
        stacks = [(0, 0, "red"), (0, 0, "blue")]
        ans_list = [float("inf") for x in range(n)]
        red_visited = [True for x in range(n)]
        blue_visited = [True for x in range(n)]
        red_visited[0] = False
        blue_visited[0] = False

        while stacks:
            curr_node, total_step, red_blue = stacks.pop(0)
            if red_blue == "red":
                if red_node_dict.get(curr_node) is not None:
                    for x in red_node_dict[curr_node]:
                        if red_visited[x]:
                            red_visited[x] = False
                            stacks.append((x, total_step + 1, "blue"))
                            ans_list[x] = min(ans_list[x], total_step + 1)
            else:
                if blue_node_dict.get(curr_node) is not None:
                    for x in blue_node_dict[curr_node]:
                        if blue_visited[x]:
                            blue_visited[x] = False
                            stacks.append((x, total_step + 1, "red"))
                            ans_list[x] = min(ans_list[x], total_step + 1)

        ans_list = [-1 if x == float("inf") else x for x in ans_list]

        # 第一个元素始终为0
        ans_list[0] = 0

        return ans_list
