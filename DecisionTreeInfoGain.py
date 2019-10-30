import csv
import math
import statistics

outputFile = open("output.txt", "w")


def open_file(file_name):
    return open(file_name)


def calculate_entropy(total, cList):
    entropy = 0
    for column in cList:
        if column != 0:
            entropy = entropy + (column/total)*math.log2((column/total))
    return abs(entropy)


fileName = "FlagData.csv"

flagFile = open(fileName)

catholicSum = 0
christianSum = 0
muslimSum = 0
buddhistSum = 0
hinduSum = 0
ethnicSum = 0
marxistSum = 0
otherSum = 0

catholicRed = 0
christianRed = 0
muslimRed = 0
buddhistRed = 0
hinduRed = 0
ethnicRed = 0
marxistRed = 0
otherRed = 0

for row in csv.reader(flagFile):
    if row:
        if row[6] == "0":
            catholicSum = catholicSum + 1
            if row[10] == "1":
                catholicRed = catholicRed + 1
        elif row[6] == "1":
            christianSum = christianSum + 1
            if row[10] == "1":
                christianRed = christianRed + 1
        elif row[6] == "2":
            muslimSum = muslimSum + 1
            if row[10] == "1":
                muslimRed = muslimRed + 1
        elif row[6] == "3":
            buddhistSum = buddhistSum + 1
            if row[10] == "1":
                buddhistRed = buddhistRed + 1
        elif row[6] == "4":
            hinduSum = hinduSum + 1
            if row[10] == "1":
                hinduRed = hinduRed + 1
        elif row[6] == "5":
            ethnicSum = ethnicSum + 1
            if row[10] == "1":
                ethnicRed = ethnicRed + 1
        elif row[6] == "6":
            marxistSum = marxistSum + 1
            if row[10] == "1":
                marxistRed = marxistRed + 1
        else:
            otherSum = otherSum + 1
            if row[10] == "1":
                otherRed = otherRed + 1

print("                                           Red             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicRed, "     |     ", catholicSum - catholicRed)
print("Christian             ", christianSum, "   |     ", christianRed, "     |     ", christianSum - christianRed)
print("Muslim                ", muslimSum, "   |     ", muslimRed, "     |     ", muslimSum - muslimRed)
print("Buddhist              ", buddhistSum, "    |     ", buddhistRed, "      |     ", buddhistSum - buddhistRed)
print("Hindu                 ", hinduSum, "    |     ", hinduRed, "      |     ", hinduSum - hinduRed)
print("Ethnic                ", ethnicSum, "   |     ", ethnicRed, "     |     ", ethnicSum - ethnicRed)
print("Marxist               ", marxistSum, "   |     ", marxistRed, "     |     ", marxistSum - marxistRed)
print("Others                ", otherSum, "    |     ", otherRed, "      |     ", otherSum - otherRed)

valList = [catholicRed, catholicSum-catholicRed]
entropyCatholic = calculate_entropy(catholicSum, valList)
print(entropyCatholic)
entropyChristian = calculate_entropy(christianSum, [christianRed, christianSum - christianRed])
print(entropyChristian)
entropyMuslim = calculate_entropy(muslimSum, [muslimRed, muslimSum - muslimRed])
print(entropyMuslim)
entropyBuddhist = calculate_entropy(buddhistSum, [buddhistRed, buddhistSum - buddhistRed])
print(entropyBuddhist)
entropyHindu = calculate_entropy(hinduSum, [hinduRed, hinduSum - hinduRed])
print(entropyHindu)
entropyEthnic = calculate_entropy(ethnicSum, [ethnicRed, ethnicSum - ethnicRed])
print(entropyEthnic)
entropyMarxist = calculate_entropy(marxistSum, [marxistRed, marxistSum - marxistRed])
print(entropyMarxist)
entropyOther = calculate_entropy(otherSum, [otherRed, otherSum - otherRed])
print(entropyOther)
