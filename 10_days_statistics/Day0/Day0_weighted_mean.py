# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(float, input().split()))
W = list(map(float, input().split()))

print(round(sum([a * b for a, b in zip(X, W)]) / sum(W),1))
