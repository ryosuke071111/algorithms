def longest_palindrome_subsequence(s):
    n = len(s)
    dp = [[0] * (n + 1) for i in range(n)]    # [i,i + j)での最長の回文の文字数
    for i in range(0, n):
        dp[i][1] = 1

    for j in range(2, n + 1):
        for i in range(n - j + 1):
            if s[i] == s[i + j - 1]:
                dp[i][j] = dp[i + 1][j - 2] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1])
    print(dp)
    return dp[0][-1]


def main():
    s = "character"
    print(longest_palindrome_subsequence(s))


if __name__ == '__main__':
    main()
