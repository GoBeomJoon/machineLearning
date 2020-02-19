__author__ = 'mike bowles'
import urllib.request
import sys
import ssl

context = ssl._create_unverified_context()

#UCI 데이터 레포지토리에서 데이터 읽기
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar"
              ".all-data")

data = urllib.request.urlopen(target_url, context=context)

#레이블을 리스트로, 속성을 리스트의 리스트로 데이터 정도
line = ''
xList = []
labels = []

for line in data:
    #쉼표로 분리

    line = line.decode()

    row = line.strip().split(",")
    xList.append(row)

sys.stdout.write("Number of Row of Data = " + str(len(xList)) + "\n")
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))

