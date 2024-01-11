# #백준 15708
n, t, p = map(int, input().split())
sumStone = 0
cnt = 0
maxTemp = 0
tempList = []

tt = list(map(int, input().split()))

for i in range(n):
    sumStone += tt[i]
    cnt += 1
    tempList.append(tt[i])
    #내림차순으로 정렬하기
    tempList.sort(reverse=True)


    while sumStone > t - p * i and cnt > 0:
        if t - p * i < 0:
            sumStone = 0
            cnt = 0
            break
        cnt -= 1
        sumStone -= tempList[0]
        tempList.pop(0)

    if maxTemp < cnt:
        maxTemp = cnt


print(maxTemp)