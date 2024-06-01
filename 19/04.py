import sys
text = filter(lambda x: x.strip()[0] == "#", sys.stdin)
print(len(list(text)))