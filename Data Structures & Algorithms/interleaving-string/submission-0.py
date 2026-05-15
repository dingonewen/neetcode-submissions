class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n + 1):
                option_1 = dp[j] and s1[i-1] == s3[i + j - 1]
                option_2 = dp[j-1] and s2[j-1] == s3[i + j - 1]

                dp[j] = option_1 or option_2

        return dp[n]
        