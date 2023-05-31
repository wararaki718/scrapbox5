import numpy as np


def longest_common_substring(s1: str, s2: str) -> int:
    dp = np.zeros((len(s1)+1, len(s2)+1))
    distance = 0
    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                dp[i+1][j+1] = dp[i][j] + 1
                distance = max(distance, dp[i+1][j+1])
    return distance


def levenshtein_distance(s1: str, s2: str) -> int:
    dp = np.zeros((len(s1)+1, len(s2)+1), dtype=int)

    for i in range(1, dp.shape[0]+1):
        dp[i][0] = i
    
    for j in range(1, dp.shape[1]+1):
        dp[0][j] = j
    
    for j, c2 in enumerate(s2, start=1):
        for i, c1 in enumerate(s1, start=1):
            cost = int(c1 == c2)
            dp[i][j] = min(
                dp[i-1][j]+1, # deletion
                dp[i][j-1]+1, # insertion
                dp[i-1][j-1]+cost # substitution
            )
    return dp[-1][-1]


def hamming_distance(s1: str, s2: str) -> int:
    distance = 0
    for c1, c2 in zip(s1, s2):
        distance += int(c1 != c2)
    return distance
