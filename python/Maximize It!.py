# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

possibleValues=[]
n,m = map(int, input().split())


for a in range(n):
    string=input()
    possibleValues.append(string.split())

tuplesList=[p for p in itertools.product(*possibleValues)]

weWantList=[]

for element in tuplesList:
    s=0
    for elem in element:
        s+=((int(elem)**2)%m)
    weWantList.append(s%m)
print(max(weWantList))