__author__ = 'mike bowles'

import urllib.request
import sys
import ssl

context = ssl._create_unverified_context()

# UCI 데이터 레포지토리에서 데이터 읽기
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar"
              ".all-data")

data = urllib.request.urlopen(target_url, context=context)

# 레이블을 리스트로, 속성을 리스트의 리스트로 데이터 정도
line = ''
xList = []
labels = []

for line in data:
    # 쉼표로 분리
    line = line.decode()
    row = line.strip().split(",")
    xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3
colCounts = []

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)
    type = [0] * 3

sys.stdout.write("Col #" + "\t" + "Number" + "\t" + "Strings" + "\t" + "Other\n")

iCol = 0;
for types in colCounts:
    sys.stdout.write(str(iCol) + "\t\t" + str(types[0]) + "\t\t" + str(types[1]) + "\t\t" + str(types[2]) + "\n")
    iCol += 1

