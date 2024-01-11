#백준 2566번


maxNum = [0,0,0]
numList = []
for i in range(9):
    num = input().split(" ")
    numList.append(num)
for i in range(9):
    for j in range(9):
        if maxNum[0] < int(numList[i][j]):
            maxNum = int(numList[i][j]),i,j
print(maxNum[0])
print(maxNum[1]+1,maxNum[2]+1)