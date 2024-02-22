import random

words = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
]


firstquestion = random.randint(0,5)
secondquestion = firstquestion

while secondquestion == firstquestion:
  secondquestion = random.randint(0,5)

thirdquestion = firstquestion

while thirdquestion == firstquestion or thirdquestion == secondquestion:
  thirdquestion = random.randint(0,5)

print("Firstquestion :")
print(words[firstquestion])
print("Secondquestion :")
print(words[secondquestion])
print("Thirdquestion :")
print(words[thirdquestion])

#input file
fin = open("data.txt", "rt")
#output file to write the result to
fout = open("index.php", "wt")
#for each line in the input file
for line in fin:
    fout.write(line.replace('question1', words[firstquestion]).replace('question2', words[secondquestion]).replace('question3', words[thirdquestion]))
#close input and output files
fin.close()
fout.close()