def make_one(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # 현재 숫자에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

n = int(input())
result = make_one(n)
print(result)
