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

firstquestion = random.randint(0, len(words) - 1)
secondquestion = firstquestion

while secondquestion == firstquestion:
    secondquestion = random.randint(0, len(words) - 1)

thirdquestion = firstquestion

while thirdquestion == firstquestion or thirdquestion == secondquestion:
    thirdquestion = random.randint(0, len(words) - 1)

print("First question:")
print(words[firstquestion])
print("Second question:")
print(words[secondquestion])
print("Third question:")
print(words[thirdquestion])

# Input file
with open("data.txt", "rt") as fin:
    data = fin.read()

# Output file to write the result to
with open("index.php", "wt") as fout:
    fout.write(
        data.replace("question1", words[firstquestion])
        .replace("question2", words[secondquestion])
        .replace("question3", words[thirdquestion])
    )
