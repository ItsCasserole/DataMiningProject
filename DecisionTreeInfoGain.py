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
            entropy = entropy + -1*(column/total)*math.log2(column/total)
    return entropy


def calculate_column_entropy(total, cList):
    entropy = 0
    for column in cList:
        entropy = entropy + (column[0]/total)*calculate_entropy(column[0], column[1:])
    return entropy;


def calculate_parent_entropy(total, cList):
    entropy = 0
    for column in cList:
        if column != 0:
            entropy = entropy + -1*(column/total)*math.log2(column/total)
    return entropy


fileName = "FlagData.csv"

flagFile = open(fileName)

totalSum = 0

catholicSum = 0
catholicRed = 0
catholicGreen = 0
catholicBlue = 0
catholicGold = 0
catholicWhite = 0
catholicBlack = 0
catholicOrange = 0
catholicCrescent = 0
catholicTriangle = 0
catholicIcon = 0
catholicAnimate = 0
catholicText = 0

christianSum = 0
christianRed = 0
christianGreen = 0
christianBlue = 0
christianGold = 0
christianWhite = 0
christianBlack = 0
christianOrange = 0
christianCrescent = 0
christianTriangle = 0
christianIcon = 0
christianAnimate = 0
christianText = 0

muslimSum = 0
muslimRed = 0
muslimGreen = 0
muslimBlue = 0
muslimGold = 0
muslimWhite = 0
muslimBlack = 0
muslimOrange = 0
muslimCrescent = 0
muslimTriangle = 0
muslimIcon = 0
muslimAnimate = 0
muslimText = 0

buddhistSum = 0
buddhistRed = 0
buddhistGreen = 0
buddhistBlue = 0
buddhistGold = 0
buddhistWhite = 0
buddhistBlack = 0
buddhistOrange = 0
buddhistCrescent = 0
buddhistTriangle = 0
buddhistIcon = 0
buddhistAnimate = 0
buddhistText = 0

hinduSum = 0
hinduRed = 0
hinduGreen = 0
hinduBlue = 0
hinduGold = 0
hinduWhite = 0
hinduBlack = 0
hinduOrange = 0
hinduCrescent = 0
hinduTriangle = 0
hinduIcon = 0
hinduAnimate = 0
hinduText = 0

ethnicSum = 0
ethnicRed = 0
ethnicGreen = 0
ethnicBlue = 0
ethnicGold = 0
ethnicWhite = 0
ethnicBlack = 0
ethnicOrange = 0
ethnicCrescent = 0
ethnicTriangle = 0
ethnicIcon = 0
ethnicAnimate = 0
ethnicText = 0

marxistSum = 0
marxistRed = 0
marxistGreen = 0
marxistBlue = 0
marxistGold = 0
marxistWhite = 0
marxistBlack = 0
marxistOrange = 0
marxistCrescent = 0
marxistTriangle = 0
marxistIcon = 0
marxistAnimate = 0
marxistText = 0

otherSum = 0
otherRed = 0
otherGreen = 0
otherBlue = 0
otherGold = 0
otherWhite = 0
otherBlack = 0
otherOrange = 0
otherCrescent = 0
otherTriangle = 0
otherIcon = 0
otherAnimate = 0
otherText = 0

for row in csv.reader(flagFile):
    if row:
        totalSum = totalSum + 1
        if row[6] == "0":
            catholicSum = catholicSum + 1
            if row[10] == "1":
                catholicRed = catholicRed + 1
            if row[11] == "1":
                catholicGreen = catholicGreen + 1
            if row[12] == "1":
                catholicBlue = catholicBlue + 1
            if row[13] == "1":
                catholicGold = catholicGold + 1
            if row[14] == "1":
                catholicWhite = catholicWhite + 1
            if row[15] == "1":
                catholicBlack = catholicBlack + 1
            if row[16] == "1":
                catholicOrange = catholicOrange + 1
            if row[23] == "1":
                catholicCrescent = catholicCrescent + 1
            if row[24] == "1":
                catholicTriangle = catholicTriangle + 1
            if row[25] == "1":
                catholicIcon = catholicIcon + 1
            if row[26] == "1":
                catholicAnimate = catholicAnimate + 1
            if row[27] == "1":
                catholicText = catholicText + 1
        elif row[6] == "1":
            christianSum = christianSum + 1
            if row[10] == "1":
                christianRed = christianRed + 1
            if row[11] == "1":
                christianGreen = christianGreen + 1
            if row[12] == "1":
                christianBlue = christianBlue + 1
            if row[13] == "1":
                christianGold = christianGold + 1
            if row[14] == "1":
                christianWhite = christianWhite + 1
            if row[15] == "1":
                christianBlack = christianBlack + 1
            if row[16] == "1":
                christianOrange = christianOrange + 1
            if row[23] == "1":
                christianCrescent = christianCrescent + 1
            if row[24] == "1":
                christianTriangle = christianTriangle + 1
            if row[25] == "1":
                christianIcon = christianIcon + 1
            if row[26] == "1":
                christianAnimate = christianAnimate + 1
            if row[27] == "1":
                christianText = christianText + 1
        elif row[6] == "2":
            muslimSum = muslimSum + 1
            if row[10] == "1":
                muslimRed = muslimRed + 1
            if row[11] == "1":
                muslimGreen = muslimGreen + 1
            if row[12] == "1":
                muslimBlue = muslimBlue + 1
            if row[13] == "1":
                muslimGold = muslimGold + 1
            if row[14] == "1":
                muslimWhite = muslimWhite + 1
            if row[15] == "1":
                muslimBlack = muslimBlack + 1
            if row[16] == "1":
                muslimOrange = muslimOrange + 1
            if row[23] == "1":
                muslimCrescent = muslimCrescent + 1
            if row[24] == "1":
                muslimTriangle = muslimTriangle + 1
            if row[25] == "1":
                muslimIcon = muslimIcon + 1
            if row[26] == "1":
                muslimAnimate = muslimAnimate + 1
            if row[27] == "1":
                muslimText = muslimText + 1
        elif row[6] == "3":
            buddhistSum = buddhistSum + 1
            if row[10] == "1":
                buddhistRed = buddhistRed + 1
            if row[11] == "1":
                buddhistGreen = buddhistGreen + 1
            if row[12] == "1":
                buddhistBlue = buddhistBlue + 1
            if row[13] == "1":
                buddhistGold = buddhistGold + 1
            if row[14] == "1":
                buddhistWhite = buddhistWhite + 1
            if row[15] == "1":
                buddhistBlack = buddhistBlack + 1
            if row[16] == "1":
                buddhistOrange = buddhistOrange + 1
            if row[23] == "1":
                buddhistCrescent = buddhistCrescent + 1
            if row[24] == "1":
                buddhistTriangle = buddhistTriangle + 1
            if row[25] == "1":
                buddhistIcon = buddhistIcon + 1
            if row[26] == "1":
                buddhistAnimate = buddhistAnimate + 1
            if row[27] == "1":
                buddhistText = buddhistText + 1
        elif row[6] == "4":
            hinduSum = hinduSum + 1
            if row[10] == "1":
                hinduRed = hinduRed + 1
            if row[11] == "1":
                hinduGreen = hinduGreen + 1
            if row[12] == "1":
                hinduBlue = hinduBlue + 1
            if row[13] == "1":
                hinduGold = hinduGold + 1
            if row[14] == "1":
                hinduWhite = hinduWhite + 1
            if row[15] == "1":
                hinduBlack = hinduBlack + 1
            if row[16] == "1":
                hinduOrange = hinduOrange + 1
            if row[23] == "1":
                hinduCrescent = hinduCrescent + 1
            if row[24] == "1":
                hinduTriangle = hinduTriangle + 1
            if row[25] == "1":
                hinduIcon = hinduIcon + 1
            if row[26] == "1":
                hinduAnimate = hinduAnimate + 1
            if row[27] == "1":
                hinduText = hinduText + 1
        elif row[6] == "5":
            ethnicSum = ethnicSum + 1
            if row[10] == "1":
                ethnicRed = ethnicRed + 1
            if row[11] == "1":
                ethnicGreen = ethnicGreen + 1
            if row[12] == "1":
                ethnicBlue = ethnicBlue + 1
            if row[13] == "1":
                ethnicGold = ethnicGold + 1
            if row[14] == "1":
                ethnicWhite = ethnicWhite + 1
            if row[15] == "1":
                ethnicBlack = ethnicBlack + 1
            if row[16] == "1":
                ethnicOrange = ethnicOrange + 1
            if row[23] == "1":
                ethnicCrescent = ethnicCrescent + 1
            if row[24] == "1":
                ethnicTriangle = ethnicTriangle + 1
            if row[25] == "1":
                ethnicIcon = ethnicIcon + 1
            if row[26] == "1":
                ethnicAnimate = ethnicAnimate + 1
            if row[27] == "1":
                ethnicText = ethnicText + 1
        elif row[6] == "6":
            marxistSum = marxistSum + 1
            if row[10] == "1":
                marxistRed = marxistRed + 1
            if row[11] == "1":
                marxistGreen = marxistGreen + 1
            if row[12] == "1":
                marxistBlue = marxistBlue + 1
            if row[13] == "1":
                marxistGold = marxistGold + 1
            if row[14] == "1":
                marxistWhite = marxistWhite + 1
            if row[15] == "1":
                marxistBlack = marxistBlack + 1
            if row[16] == "1":
                marxistOrange = marxistOrange + 1
            if row[23] == "1":
                marxistCrescent = marxistCrescent + 1
            if row[24] == "1":
                marxistTriangle = marxistTriangle + 1
            if row[25] == "1":
                marxistIcon = marxistIcon + 1
            if row[26] == "1":
                marxistAnimate = marxistAnimate + 1
            if row[27] == "1":
                marxistText = marxistText + 1
        elif row[6] == "7":
            otherSum = otherSum + 1
            if row[10] == "1":
                otherRed = otherRed + 1
            if row[11] == "1":
                otherGreen = otherGreen + 1
            if row[12] == "1":
                otherBlue = otherBlue + 1
            if row[13] == "1":
                otherGold = otherGold + 1
            if row[14] == "1":
                otherWhite = otherWhite + 1
            if row[15] == "1":
                otherBlack = otherBlack + 1
            if row[16] == "1":
                otherOrange = otherOrange + 1
            if row[23] == "1":
                otherCrescent = otherCrescent + 1
            if row[24] == "1":
                otherTriangle = otherTriangle + 1
            if row[25] == "1":
                otherIcon = otherIcon + 1
            if row[26] == "1":
                otherAnimate = otherAnimate + 1
            if row[27] == "1":
                otherText = otherText + 1

parentEntropy = calculate_parent_entropy(totalSum, [catholicSum, christianSum, muslimSum, buddhistSum,
                                                    hinduSum, ethnicSum, marxistSum, otherSum])
print("Parent Entropy: ", parentEntropy)
print()
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
print()
print("                                          Green             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicGreen, "     |     ", catholicSum - catholicGreen)
print("Christian             ", christianSum, "   |     ", christianGreen, "     |     ", christianSum - christianGreen)
print("Muslim                ", muslimSum, "   |     ", muslimGreen, "     |     ", muslimSum - muslimGreen)
print("Buddhist              ", buddhistSum, "    |     ", buddhistGreen, "      |     ", buddhistSum - buddhistGreen)
print("Hindu                 ", hinduSum, "    |     ", hinduGreen, "      |     ", hinduSum - hinduGreen)
print("Ethnic                ", ethnicSum, "   |     ", ethnicGreen, "     |     ", ethnicSum - ethnicGreen)
print("Marxist               ", marxistSum, "   |     ", marxistGreen, "      |     ", marxistSum - marxistGreen)
print("Others                ", otherSum, "    |     ", otherGreen, "      |     ", otherSum - otherGreen)
print()
print("                                           Blue             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicBlue, "     |     ", catholicSum - catholicBlue)
print("Christian             ", christianSum, "   |     ", christianBlue, "     |     ", christianSum - christianBlue)
print("Muslim                ", muslimSum, "   |     ", muslimBlue, "      |     ", muslimSum - muslimBlue)
print("Buddhist              ", buddhistSum, "    |     ", buddhistBlue, "      |     ", buddhistSum - buddhistBlue)
print("Hindu                 ", hinduSum, "    |     ", hinduBlue, "      |     ", hinduSum - hinduBlue)
print("Ethnic                ", ethnicSum, "   |     ", ethnicBlue, "     |     ", ethnicSum - ethnicBlue)
print("Marxist               ", marxistSum, "   |     ", marxistBlue, "      |     ", marxistSum - marxistBlue)
print("Others                ", otherSum, "    |     ", otherBlue, "      |     ", otherSum - otherBlue)
print()
print("                                           Gold             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicGold, "     |     ", catholicSum - catholicGold)
print("Christian             ", christianSum, "   |     ", christianGold, "     |     ", christianSum - christianGold)
print("Muslim                ", muslimSum, "   |     ", muslimGold, "      |     ", muslimSum - muslimGold)
print("Buddhist              ", buddhistSum, "    |     ", buddhistGold, "      |     ", buddhistSum - buddhistGold)
print("Hindu                 ", hinduSum, "    |     ", hinduGold, "      |     ", hinduSum - hinduGold)
print("Ethnic                ", ethnicSum, "   |     ", ethnicGold, "     |     ", ethnicSum - ethnicGold)
print("Marxist               ", marxistSum, "   |     ", marxistGold, "      |     ", marxistSum - marxistGold)
print("Others                ", otherSum, "    |     ", otherGold, "      |     ", otherSum - otherGold)
print()
print("                                          White             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicWhite, "     |     ", catholicSum - catholicWhite)
print("Christian             ", christianSum, "   |     ", christianWhite, "     |     ", christianSum - christianWhite)
print("Muslim                ", muslimSum, "   |     ", muslimWhite, "     |     ", muslimSum - muslimWhite)
print("Buddhist              ", buddhistSum, "    |     ", buddhistWhite, "      |     ", buddhistSum - buddhistWhite)
print("Hindu                 ", hinduSum, "    |     ", hinduWhite, "      |     ", hinduSum - hinduWhite)
print("Ethnic                ", ethnicSum, "   |     ", ethnicWhite, "     |     ", ethnicSum - ethnicWhite)
print("Marxist               ", marxistSum, "   |     ", marxistWhite, "      |     ", marxistSum - marxistWhite)
print("Others                ", otherSum, "    |     ", otherWhite, "      |     ", otherSum - otherWhite)
print()
print("                                          Black             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicBlack, "      |     ", catholicSum - catholicBlack)
print("Christian             ", christianSum, "   |     ", christianBlack, "     |     ", christianSum - christianBlack)
print("Muslim                ", muslimSum, "   |     ", muslimBlack, "     |     ", muslimSum - muslimBlack)
print("Buddhist              ", buddhistSum, "    |     ", buddhistBlack, "      |     ", buddhistSum - buddhistBlack)
print("Hindu                 ", hinduSum, "    |     ", hinduBlack, "      |     ", hinduSum - hinduBlack)
print("Ethnic                ", ethnicSum, "   |     ", ethnicBlack, "     |     ", ethnicSum - ethnicBlack)
print("Marxist               ", marxistSum, "   |     ", marxistBlack, "      |     ", marxistSum - marxistBlack)
print("Others                ", otherSum, "    |     ", otherBlack, "      |     ", otherSum - otherBlack)
print()
print("                                          Orange             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicOrange, "      |     ", catholicSum - catholicOrange)
print("Christian             ", christianSum, "   |     ", christianOrange, "     |     ", christianSum - christianOrange)
print("Muslim                ", muslimSum, "   |     ", muslimOrange, "      |     ", muslimSum - muslimOrange)
print("Buddhist              ", buddhistSum, "    |     ", buddhistOrange, "      |     ", buddhistSum - buddhistOrange)
print("Hindu                 ", hinduSum, "    |     ", hinduOrange, "      |     ", hinduSum - hinduOrange)
print("Ethnic                ", ethnicSum, "   |     ", ethnicOrange, "      |     ", ethnicSum - ethnicOrange)
print("Marxist               ", marxistSum, "   |     ", marxistOrange, "      |     ", marxistSum - marxistOrange)
print("Others                ", otherSum, "    |     ", otherOrange, "      |     ", otherSum - otherOrange)
print()
print("                                          Crescent             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicCrescent, "      |     ", catholicSum - catholicCrescent)
print("Christian             ", christianSum, "   |     ", christianCrescent, "      |     ", christianSum - christianCrescent)
print("Muslim                ", muslimSum, "   |     ", muslimCrescent, "      |     ", muslimSum - muslimCrescent)
print("Buddhist              ", buddhistSum, "    |     ", buddhistCrescent, "      |     ", buddhistSum - buddhistCrescent)
print("Hindu                 ", hinduSum, "    |     ", hinduCrescent, "      |     ", hinduSum - hinduCrescent)
print("Ethnic                ", ethnicSum, "   |     ", ethnicCrescent, "      |     ", ethnicSum - ethnicCrescent)
print("Marxist               ", marxistSum, "   |     ", marxistCrescent, "      |     ", marxistSum - marxistCrescent)
print("Others                ", otherSum, "    |     ", otherCrescent, "      |     ", otherSum - otherCrescent)
print()
print("                                          Triangle             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicTriangle, "      |     ", catholicSum - catholicTriangle)
print("Christian             ", christianSum, "   |     ", christianTriangle, "     |     ", christianSum - christianTriangle)
print("Muslim                ", muslimSum, "   |     ", muslimTriangle, "      |     ", muslimSum - muslimTriangle)
print("Buddhist              ", buddhistSum, "    |     ", buddhistTriangle, "      |     ", buddhistSum - buddhistTriangle)
print("Hindu                 ", hinduSum, "    |     ", hinduTriangle, "      |     ", hinduSum - hinduTriangle)
print("Ethnic                ", ethnicSum, "   |     ", ethnicTriangle, "      |     ", ethnicSum - ethnicTriangle)
print("Marxist               ", marxistSum, "   |     ", marxistTriangle, "      |     ", marxistSum - marxistTriangle)
print("Others                ", otherSum, "    |     ", otherTriangle, "      |     ", otherSum - otherTriangle)
print()
print("                                          Icon             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicIcon, "      |     ", catholicSum - catholicIcon)
print("Christian             ", christianSum, "   |     ", christianIcon, "     |     ", christianSum - christianIcon)
print("Muslim                ", muslimSum, "   |     ", muslimIcon, "      |     ", muslimSum - muslimIcon)
print("Buddhist              ", buddhistSum, "    |     ", buddhistIcon, "      |     ", buddhistSum - buddhistIcon)
print("Hindu                 ", hinduSum, "    |     ", hinduIcon, "      |     ", hinduSum - hinduIcon)
print("Ethnic                ", ethnicSum, "   |     ", ethnicIcon, "      |     ", ethnicSum - ethnicIcon)
print("Marxist               ", marxistSum, "   |     ", marxistIcon, "      |     ", marxistSum - marxistIcon)
print("Others                ", otherSum, "    |     ", otherIcon, "      |     ", otherSum - otherIcon)
print()
print("                                          Animate             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicAnimate, "      |     ", catholicSum - catholicAnimate)
print("Christian             ", christianSum, "   |     ", christianAnimate, "     |     ", christianSum - christianAnimate)
print("Muslim                ", muslimSum, "   |     ", muslimAnimate, "      |     ", muslimSum - muslimAnimate)
print("Buddhist              ", buddhistSum, "    |     ", buddhistAnimate, "      |     ", buddhistSum - buddhistAnimate)
print("Hindu                 ", hinduSum, "    |     ", hinduAnimate, "      |     ", hinduSum - hinduAnimate)
print("Ethnic                ", ethnicSum, "   |     ", ethnicAnimate, "      |     ", ethnicSum - ethnicAnimate)
print("Marxist               ", marxistSum, "   |     ", marxistAnimate, "      |     ", marxistSum - marxistAnimate)
print("Others                ", otherSum, "    |     ", otherAnimate, "      |     ", otherSum - otherAnimate)
print()
print("                                          Text             ")
print("                    Total    |     Yes      |      No      ")
print("Catholic              ", catholicSum, "   |     ", catholicText, "      |     ", catholicSum - catholicText)
print("Christian             ", christianSum, "   |     ", christianText, "      |     ", christianSum - christianText)
print("Muslim                ", muslimSum, "   |     ", muslimText, "      |     ", muslimSum - muslimText)
print("Buddhist              ", buddhistSum, "    |     ", buddhistText, "      |     ", buddhistSum - buddhistText)
print("Hindu                 ", hinduSum, "    |     ", hinduText, "      |     ", hinduSum - hinduText)
print("Ethnic                ", ethnicSum, "   |     ", ethnicText, "      |     ", ethnicSum - ethnicText)
print("Marxist               ", marxistSum, "   |     ", marxistText, "      |     ", marxistSum - marxistText)
print("Others                ", otherSum, "    |     ", otherText, "      |     ", otherSum - otherText)
print()
catholicRedList = [catholicSum, catholicRed, catholicSum - catholicRed]
christianRedList = [christianSum, christianRed, christianSum - christianRed]
muslimRedList = [muslimSum, muslimRed, muslimSum - muslimRed]
buddhistRedList = [buddhistSum, buddhistRed, buddhistSum - buddhistRed]
hinduRedList = [hinduSum, hinduRed, hinduSum - hinduRed]
ethnicRedList = [ethnicSum, ethnicRed, ethnicSum - ethnicRed]
marxistRedList = [marxistSum, marxistRed, marxistSum - marxistRed]
otherRedList = [otherSum, otherRed, otherSum - otherRed]

redEntropy = calculate_column_entropy(totalSum, [catholicRedList, christianRedList, muslimRedList, buddhistRedList,
                                                 hinduRedList, ethnicRedList, marxistRedList, otherRedList])

redInfoGain = parentEntropy - redEntropy

print("Religion Red Information Gain: ", redInfoGain)

catholicGreenList = [catholicSum, catholicGreen, catholicSum - catholicGreen]
christianGreenList = [christianSum, christianGreen, christianSum - christianGreen]
muslimGreenList = [muslimSum, muslimGreen, muslimSum - muslimGreen]
buddhistGreenList = [buddhistSum, buddhistGreen, buddhistSum - buddhistGreen]
hinduGreenList = [hinduSum, hinduGreen, hinduSum - hinduGreen]
ethnicGreenList = [ethnicSum, ethnicGreen, ethnicSum - ethnicGreen]
marxistGreenList = [marxistSum, marxistGreen, marxistSum - marxistGreen]
otherGreenList = [otherSum, otherGreen, otherSum - otherGreen]

greenEntropy = calculate_column_entropy(totalSum, [catholicGreenList, christianGreenList, muslimGreenList, buddhistGreenList,
                                                   hinduGreenList, ethnicGreenList, marxistGreenList, otherGreenList])

greenInfoGain = parentEntropy - greenEntropy

print("Religion Green Information Gain: ", greenInfoGain)

catholicBlueList = [catholicSum, catholicBlue, catholicSum - catholicBlue]
christianBlueList = [christianSum, christianBlue, christianSum - christianBlue]
muslimBlueList = [muslimSum, muslimBlue, muslimSum - muslimBlue]
buddhistBlueList = [buddhistSum, buddhistBlue, buddhistSum - buddhistBlue]
hinduBlueList = [hinduSum, hinduBlue, hinduSum - hinduBlue]
ethnicBlueList = [ethnicSum, ethnicBlue, ethnicSum - ethnicBlue]
marxistBlueList = [marxistSum, marxistBlue, marxistSum - marxistBlue]
otherBlueList = [otherSum, otherBlue, otherSum - otherBlue]

blueEntropy = calculate_column_entropy(totalSum, [catholicBlueList, christianBlueList, muslimBlueList, buddhistBlueList,
                                                  hinduBlueList, ethnicBlueList, marxistBlueList, otherBlueList])

blueInfoGain = parentEntropy - blueEntropy

print("Religion Blue Information Gain: ", blueInfoGain)

catholicGoldList = [catholicSum, catholicGold, catholicSum - catholicGold]
christianGoldList = [christianSum, christianGold, christianSum - christianGold]
muslimGoldList = [muslimSum, muslimGold, muslimSum - muslimGold]
buddhistGoldList = [buddhistSum, buddhistGold, buddhistSum - buddhistGold]
hinduGoldList = [hinduSum, hinduGold, hinduSum - hinduGold]
ethnicGoldList = [ethnicSum, ethnicGold, ethnicSum - ethnicGold]
marxistGoldList = [marxistSum, marxistGold, marxistSum - marxistGold]
otherGoldList = [otherSum, otherGold, otherSum - otherGold]

goldEntropy = calculate_column_entropy(totalSum, [catholicGoldList, christianGoldList, muslimGoldList, buddhistGoldList,
                                                  hinduGoldList, ethnicGoldList, marxistGoldList, otherGoldList])

goldInfoGain = parentEntropy - goldEntropy

print("Religion Gold Information Gain: ", goldInfoGain)

catholicWhiteList = [catholicSum, catholicWhite, catholicSum - catholicWhite]
christianWhiteList = [christianSum, christianWhite, christianSum - christianWhite]
muslimWhiteList = [muslimSum, muslimWhite, muslimSum - muslimWhite]
buddhistWhiteList = [buddhistSum, buddhistWhite, buddhistSum - buddhistWhite]
hinduWhiteList = [hinduSum, hinduWhite, hinduSum - hinduWhite]
ethnicWhiteList = [ethnicSum, ethnicWhite, ethnicSum - ethnicWhite]
marxistWhiteList = [marxistSum, marxistWhite, marxistSum - marxistWhite]
otherWhiteList = [otherSum, otherWhite, otherSum - otherWhite]

whiteEntropy = calculate_column_entropy(totalSum, [catholicWhiteList, christianWhiteList, muslimWhiteList, buddhistWhiteList,
                                                   hinduWhiteList, ethnicWhiteList, marxistWhiteList, otherWhiteList])

whiteInfoGain = parentEntropy - whiteEntropy

print("Religion White Information Gain: ", whiteInfoGain)

catholicBlackList = [catholicSum, catholicBlack, catholicSum - catholicBlack]
christianBlackList = [christianSum, christianBlack, christianSum - christianBlack]
muslimBlackList = [muslimSum, muslimBlack, muslimSum - muslimBlack]
buddhistBlackList = [buddhistSum, buddhistBlack, buddhistSum - buddhistBlack]
hinduBlackList = [hinduSum, hinduBlack, hinduSum - hinduBlack]
ethnicBlackList = [ethnicSum, ethnicBlack, ethnicSum - ethnicBlack]
marxistBlackList = [marxistSum, marxistBlack, marxistSum - marxistBlack]
otherBlackList = [otherSum, otherBlack, otherSum - otherBlack]

blackEntropy = calculate_column_entropy(totalSum, [catholicBlackList, christianBlackList, muslimBlackList, buddhistBlackList,
                                                   hinduBlackList, ethnicBlackList, marxistBlackList, otherBlackList])

blackInfoGain = parentEntropy - blackEntropy

print("Religion Black Information Gain: ", blackInfoGain)

catholicOrangeList = [catholicSum, catholicOrange, catholicSum - catholicOrange]
christianOrangeList = [christianSum, christianOrange, christianSum - christianOrange]
muslimOrangeList = [muslimSum, muslimOrange, muslimSum - muslimOrange]
buddhistOrangeList = [buddhistSum, buddhistOrange, buddhistSum - buddhistOrange]
hinduOrangeList = [hinduSum, hinduOrange, hinduSum - hinduOrange]
ethnicOrangeList = [ethnicSum, ethnicOrange, ethnicSum - ethnicOrange]
marxistOrangeList = [marxistSum, marxistOrange, marxistSum - marxistOrange]
otherOrangeList = [otherSum, otherOrange, otherSum - otherOrange]

orangeEntropy = calculate_column_entropy(totalSum, [catholicOrangeList, christianOrangeList, muslimOrangeList, buddhistOrangeList,
                                                    hinduOrangeList, ethnicOrangeList, marxistOrangeList, otherOrangeList])

orangeInfoGain = parentEntropy - orangeEntropy

print("Religion Orange Information Gain: ", orangeInfoGain)

catholicCrescentList = [catholicSum, catholicCrescent, catholicSum - catholicCrescent]
christianCrescentList = [christianSum, christianCrescent, christianSum - christianCrescent]
muslimCrescentList = [muslimSum, muslimCrescent, muslimSum - muslimCrescent]
buddhistCrescentList = [buddhistSum, buddhistCrescent, buddhistSum - buddhistCrescent]
hinduCrescentList = [hinduSum, hinduCrescent, hinduSum - hinduCrescent]
ethnicCrescentList = [ethnicSum, ethnicCrescent, ethnicSum - ethnicCrescent]
marxistCrescentList = [marxistSum, marxistCrescent, marxistSum - marxistCrescent]
otherCrescentList = [otherSum, otherCrescent, otherSum - otherCrescent]

crescentEntropy = calculate_column_entropy(totalSum, [catholicCrescentList, christianCrescentList, muslimCrescentList, buddhistCrescentList,
                                                    hinduCrescentList, ethnicCrescentList, marxistCrescentList, otherCrescentList])

crescentInfoGain = parentEntropy - crescentEntropy

print("Religion Crescent Information Gain: ", crescentInfoGain)

catholicTriangleList = [catholicSum, catholicTriangle, catholicSum - catholicTriangle]
christianTriangleList = [christianSum, christianTriangle, christianSum - christianTriangle]
muslimTriangleList = [muslimSum, muslimTriangle, muslimSum - muslimTriangle]
buddhistTriangleList = [buddhistSum, buddhistTriangle, buddhistSum - buddhistTriangle]
hinduTriangleList = [hinduSum, hinduTriangle, hinduSum - hinduTriangle]
ethnicTriangleList = [ethnicSum, ethnicTriangle, ethnicSum - ethnicTriangle]
marxistTriangleList = [marxistSum, marxistTriangle, marxistSum - marxistTriangle]
otherTriangleList = [otherSum, otherTriangle, otherSum - otherTriangle]

triangleEntropy = calculate_column_entropy(totalSum, [catholicTriangleList, christianTriangleList, muslimTriangleList, buddhistTriangleList,
                                                    hinduTriangleList, ethnicTriangleList, marxistTriangleList, otherTriangleList])

triangleInfoGain = parentEntropy - triangleEntropy

print("Religion Triangle Information Gain: ", triangleInfoGain)

catholicIconList = [catholicSum, catholicIcon, catholicSum - catholicIcon]
christianIconList = [christianSum, christianIcon, christianSum - christianIcon]
muslimIconList = [muslimSum, muslimIcon, muslimSum - muslimIcon]
buddhistIconList = [buddhistSum, buddhistIcon, buddhistSum - buddhistIcon]
hinduIconList = [hinduSum, hinduIcon, hinduSum - hinduIcon]
ethnicIconList = [ethnicSum, ethnicIcon, ethnicSum - ethnicIcon]
marxistIconList = [marxistSum, marxistIcon, marxistSum - marxistIcon]
otherIconList = [otherSum, otherIcon, otherSum - otherIcon]

iconEntropy = calculate_column_entropy(totalSum, [catholicIconList, christianIconList, muslimIconList, buddhistIconList,
                                                    hinduIconList, ethnicIconList, marxistIconList, otherIconList])

iconInfoGain = parentEntropy - iconEntropy

print("Religion Icon Information Gain: ", iconInfoGain)

catholicAnimateList = [catholicSum, catholicAnimate, catholicSum - catholicAnimate]
christianAnimateList = [christianSum, christianAnimate, christianSum - christianAnimate]
muslimAnimateList = [muslimSum, muslimAnimate, muslimSum - muslimAnimate]
buddhistAnimateList = [buddhistSum, buddhistAnimate, buddhistSum - buddhistAnimate]
hinduAnimateList = [hinduSum, hinduAnimate, hinduSum - hinduAnimate]
ethnicAnimateList = [ethnicSum, ethnicAnimate, ethnicSum - ethnicAnimate]
marxistAnimateList = [marxistSum, marxistAnimate, marxistSum - marxistAnimate]
otherAnimateList = [otherSum, otherAnimate, otherSum - otherAnimate]

animateEntropy = calculate_column_entropy(totalSum, [catholicAnimateList, christianAnimateList, muslimAnimateList, buddhistAnimateList,
                                                    hinduAnimateList, ethnicAnimateList, marxistAnimateList, otherAnimateList])

animateInfoGain = parentEntropy - animateEntropy

print("Religion Animate Information Gain: ", animateInfoGain)

catholicTextList = [catholicSum, catholicText, catholicSum - catholicText]
christianTextList = [christianSum, christianText, christianSum - christianText]
muslimTextList = [muslimSum, muslimText, muslimSum - muslimText]
buddhistTextList = [buddhistSum, buddhistText, buddhistSum - buddhistText]
hinduTextList = [hinduSum, hinduText, hinduSum - hinduText]
ethnicTextList = [ethnicSum, ethnicText, ethnicSum - ethnicText]
marxistTextList = [marxistSum, marxistText, marxistSum - marxistText]
otherTextList = [otherSum, otherText, otherSum - otherText]

textEntropy = calculate_column_entropy(totalSum, [catholicTextList, christianTextList, muslimTextList, buddhistTextList,
                                                    hinduTextList, ethnicTextList, marxistTextList, otherTextList])

textInfoGain = parentEntropy - textEntropy

print("Religion Text Information Gain: ", textInfoGain)