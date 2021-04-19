import sys
import collections

data_in = []
for line in sys.stdin:
    data_in.append(line.split())

# print(data_in)
jingli = collections.defaultdict(str)
jingli = {}

zuyuan = collections.defaultdict(str)
zuyuan = {}

waibao = collections.defaultdict(str)
waibao = {}
# print('AAAAAAAAAAAAAA', data_in[2])
for i in range(len(data_in)):
    waibao_p = data_in[0]
    waibao_num = data_in[1]
    waibao[waibao_p] = waibao_num
    if data_in[i] == ['organization']:
        break
for j in data_in[i + 1:-1]:
    jingli_temp = j[0]
    zuyuan_temp = j[1]
    waibao_temp = j[2]
    jingli[jingli_temp] += waibao[waibao_temp]
    zuyuan[zuyuan_temp] += waibao[waibao_temp]

