score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
         "C+": 2.5, "C0": 2.0, "D+": .5, "D0": 1.0, "F": 0}

sum = 0.0
cnt = 20
for i in range(20):
    strlist = str(input())
    strpars = strlist.split(" ")
    if strpars[2] == "P":
        cnt = cnt - 1
        #print(cnt)
        continue
    sum = sum + float(score[strpars[2]])
#print(sum)
result = sum / cnt
print(result)
