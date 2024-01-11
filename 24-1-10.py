# #백준 19598
# rn = int(input())
#
# rt = []
# max = 0
#
# for i in range(rn):
#     temp = list(map(int,input().split(" ")))
#     if max < temp[1]:
#         max = temp[1]
#     rt.append(temp)
#
# room = [0 for i in range(max)]
# max = 0
#
# for i in range(len(rt)):
#
#     for j in range(rt[i][0], rt[i][1]):
#         room[j] = room[j] + 1
#         if max < room[j]:
#             max = room[j]
# print(max)
#


rn = int(input())

rt = []


for i in range(rn):
    temp = list(map(int,input().split(" ")))
    rt.append([temp[0],1])
    rt.append([temp[1],-1])
rt.sort()

result = 0
max = 0
for i in range(len(rt)):
    result = result + rt[i][1]
    if max < result:
        max = result
print(max)