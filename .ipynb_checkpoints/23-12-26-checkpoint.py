croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

strInput = list(input())
flag = 0
temp = ""
count = 0

for x in range(len(strInput)):
    if flag > 0:
        flag = flag - 1
        continue
    if x < (len(strInput) - 1) and (strInput[x] == 'c' or strInput[x] == 'd' or strInput[x] == 'l' or strInput[x] == 'n' or strInput[x] == 's' or strInput[x] == 'z'):
        temp = strInput[x]
        if x < (len(strInput) - 1):
            temp = temp + strInput[x+1]
        for y in range(len(croatia)):
            if temp == croatia[y]:
                count = count + 1
                flag = len(temp) - 1

    if x < (len(strInput) - 2) and strInput[x] == 'd' and strInput[x + 1] == 'z' and strInput[x + 2] == '=':
        count = count + 1
        flag = 2

    if flag == 0:
        count = count + 1

print(count)