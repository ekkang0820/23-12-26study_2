#백준 25206번

score = {"A+": 4.5, "A0": 4.0, "B+": 3.5,
         "B0": 3.0, "C+": 2.5, "C0": 2.0,
         "D+": 1.5, "D0": 1.0, "F": 0.0}

sum = 0.0
cnt = 0.0
for i in range(20):
    strlist = str(input())
    strpars = strlist.split(" ")
    if strpars[2] == "P":
        continue
    cnt = cnt + float(strpars[1])
    sum = sum + float(score[strpars[2]])*float(strpars[1])

print(round(sum/cnt,6))

