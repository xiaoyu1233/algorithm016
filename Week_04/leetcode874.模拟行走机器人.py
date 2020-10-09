#逻辑模拟
#set是哈希查找，list是顺序查找，所以存成set比较快
#不要直接用dir，python有自己的dir函数，虽然用了也不会出错。

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 字典存储某个方向(key)对应的 [x方向移动，y方向移动，当前方向的左侧，当前方向的右侧] (val)
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y = 0, 0
        direct = 'up'
        res = 0
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:  # 正数的话进行模型行进操作
                for step in range(command):
                    if (x + direction[direct][0], y + direction[direct][1]) not in obstacles:
                        x += direction[direct][0]
                        y += direction[direct][1]
                        res = max(res, x ** 2 + y ** 2)
                    else:
                        break
            else:  # 负数的话只改变行进方向
                if command == -1:  # 右转
                    direct = direction[direct][3]
                else:  # 即command == -2，左转
                    direct = direction[direct][2]
        return res
