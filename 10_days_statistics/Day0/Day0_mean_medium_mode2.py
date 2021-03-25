# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

filepath = './input.txt'
with open(filepath) as fp:
	N = int(fp.readline())
	X =  list(map(int, fp.readline().split()))
	
	print(np.mean(X))
	print(np.median(X))
	print(int(stats.mode(X)[0]))

