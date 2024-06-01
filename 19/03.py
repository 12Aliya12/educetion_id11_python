import sys
data = list(map(str.strip, sys.stdin))
if len(data) == 0:
    print('-1')
else:
    data = list(map(lambda x: float(x), data))
    print(sum(data) / len(data))