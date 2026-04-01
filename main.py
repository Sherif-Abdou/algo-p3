from typing import Dict

def common_subsequence(a: str, b: str, weights: Dict[str, int]):
    table = [[0 for _ in range(len(b))] for _ in range(len(a))]

    # Dynamic programming for optimal solution
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                prev = table[i-1][j-1] if i > 0 and j > 0 else 0
                table[i][j] = prev + weights[a[i]]
            else:
                prev_i = table[i-1][j] if i > 0 else 0
                prev_j = table[i][j-1] if j > 0 else 0
                table[i][j] = max(prev_i, prev_j)
    i = len(a) - 1
    j = len(b) - 1
    optimal = table[i][j]

    # Backtracking for the sequence of the solution
    tracker = ""
    while i >= 0 and j >= 0:
        if a[i] == b[j]:
            tracker = a[i] + tracker
            i -= 1
            j -= 1
        else:
            prev_i = table[i-1][j] if i > 0 else 0
            prev_j = table[i][j-1] if j > 0 else 0
            if prev_i > prev_j:
                i -= 1
            else:
                j -= 1


    return optimal, tracker

weights = {"a": 2, "b": 4, "c": 5}

optimal_value, optimal_sequence = common_subsequence("aacb", "caab", weights)
print(optimal_value, optimal_sequence)
