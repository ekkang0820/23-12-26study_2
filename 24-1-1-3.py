#백준 2738번

a,b = input().split(" ")
numList = []


for i in range(int(a)*2):
    num = input().split(" ")
    numList.append(num)

for i in range(int(a)):
    for j in range(int(b)):
        print(int(numList[i][j])+int(numList[i+int(a)][j]), end=" ")
    print()


