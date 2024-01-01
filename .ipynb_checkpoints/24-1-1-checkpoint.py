#백준 1316번

num_in = int(input())
result = num_in

strlist = [input() for i in range(num_in)]
#print(strlist)


for i in range(0,num_in):
    flag = 0
    tempstr = ""
    for j in range(0,len(strlist[i])):
        #print(strlist[i][j])
        if flag == 1:
            break
        if j > 0 and strlist[i][j-1] == strlist[i][j]:
            continue
        else:
            for z in tempstr:
                if z == strlist[i][j]:
                    result = result - 1
                    flag = 1
                    break
            tempstr = tempstr + strlist[i][j]

#print(tempstr)
print(result)
