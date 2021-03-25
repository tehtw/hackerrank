# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

N = int(input())
X = list(map(int, input().split()))
print(np.mean(X))
print(np.median(X))
print(int(stats.mode(X)[0]))

