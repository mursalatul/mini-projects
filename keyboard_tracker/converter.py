import os
# make sure your terminal running where the main.py is placed
cwd = os.path.join(os.getcwd(),'keystrock.txt')

with open(cwd, 'r') as f:
    for s in f.readlines():
        print("".join(list(map(lambda x : chr(int(x)), s.split()))))