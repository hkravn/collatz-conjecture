from matplotlib import pyplot
import sys

MAX_HEIGHT = 2000
TEST_LIMIT = 1000000

result = [[0 for i in range(MAX_HEIGHT)] for i in range(TEST_LIMIT)]

sys.setrecursionlimit(MAX_HEIGHT)

def collatz(x):
    global result
    global step
    global i
    if x==1.0:
        result[i][step] = x
        return 1
    elif (x%2)==1.0 and x!=1.0:
        result[i][step] = x
        step += 1
        return collatz(3*x+1.0)
    elif (x%2)==0.0 and x!=1.0:
        result[i][step] = x
        step += 1
        return collatz(x*0.5)
    else:
        return False

for i in range(1,TEST_LIMIT):
    step = 0
    print(i)
    collatz(i)

pyplot.plot(result)
pyplot.show()