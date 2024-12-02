import re 
with open('day1.txt', 'r') as file:
    valList = file.readlines()
# print(len(valList))
# print(valList[0])
onlyNums = [re.sub(r'\D', '', line) for line in valList]  
# print(onlyNums)

finalNums = []
for i in onlyNums:
    if len(i)< 2:
        # print(i)
        twoi = int(str(i+i))
        # print(twoi)
        finalNums.append(twoi)
        # pass
    else:
        i = list(i)
        # print(i, i[0], i[len(i)-1])
        nums = int(str(i[0]+i[len(i)-1]))
        finalNums.append(nums)

print(f'PT 1 FINAL:{sum(finalNums)}')

###############################################################################
# PT 2
import re

# dict to map words to nums
wordToNum = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
allNums = []
with open('day1.txt', 'r') as file:
    for line in file:
        line = line.lower()
        # convertToNum = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine|ten', line)
        convertToNum = re.findall(r'(?=(\d+|one|two|three|four|five|six|seven|eight|nine|ten))', line)
        #convert matches to nums
        numericVals = [int(match) if match.isdigit() else wordToNum[match] for match in convertToNum]
        # DEBUGGING Output
        # print(f"\nLine: {line.strip()}")
        # print(f"Extracted Numbers in Order: {numericVals}")
        allNums.append(numericVals)
sumAllNums2 = 0
for line in allNums: 
    newLine = int(', '.join(map(str, line)).replace(" ", "").replace(",", ""))
    # print(f'Old line:, {line}, New Line: {newLine}, length: {len(str(newLine))}, type: {type(newLine)}')
    if len(str(newLine))<2:
        # print(newLine)
        newNum = (int(str(newLine)+str(newLine)))
        # print(newNum)
        sumAllNums2+=newNum
    else:
        newLine = list(str(newLine))
        # print(newLine, newLine[0], int(newLine[-1]))
        addingThis = int(str(newLine[0]+(newLine[-1])))
        # print(addingThis)
        sumAllNums2+=addingThis

print("\n\nPT2 FINAL: ", sumAllNums2)