# #다이나믹 프로그래밍 공부
# memo = [0]*100
#
# # 피보나치 수열을 재귀함수로 구현(topdown)
# def fibo(x):
#   # fibo(1)=fibo(2)=0
#   if x==1 or x==2:
#     return 1
#
#   # 이미 계산한 적있는 문제라면 그대로 반환
#   if memo[x] != 0:
#     return memo[x]
#
#   # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#   memo[x] = fibo(x-1)+fibo(x-2)
#   return memo[x]
#
#
# print(fibo(99))

# 작은 문제부터 해결해서 저장할 dp테이블
dp = [0]*100

# fibo(1)=fibo(2)=0
dp[1]=1
dp[2]=1
n=99

# 피보나치 수열을 반복문으로 구현(bottom up)
for i in range(3, n+1):
  dp[i] = dp[i-1]+dp[i-2]

print(dp[n])