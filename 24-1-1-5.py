#백준 10978번

maxLen = 0
strList = []
for i in range(5):
    str = list(input())
    strList.append(str)

for i in range(5):
    if maxLen < len(strList[i]):
        maxLen = len(strList[i])

for i in range(maxLen):
    for j in range(5):
        if len(strList[j]) <= i :
            continue
        else:
            print(strList[j][i],end="")
