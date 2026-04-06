import argparse
import time
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

def parse_input(path):
    with open(path, "r") as f:
        alphabet_length = int(f.readline())
        weights = dict()
        for _ in range(alphabet_length):
            line = f.readline()
            key, value, *_ = line.split(" ")
            value = int(value)
            weights[key.strip()] = value
        line_a = f.readline().strip()
        line_b = f.readline().strip()
    return line_a, line_b, weights

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", action="store_true")
    parser.add_argument("-m", "--multiplier", action="store", default=1)
    parser.add_argument("path")

    args = parser.parse_args()
    multiplier = int(args.multiplier)
    line_a, line_b, weights = parse_input(args.path)
    before = time.time()
    optimal_value, optimal_sequence = common_subsequence(line_a * multiplier, line_b * multiplier, weights)
    after = time.time()
    print(optimal_value)
    print(optimal_sequence)
    if args.time:
        print(f"Time: {after - before} s")
