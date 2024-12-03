import pandas as pd
import copy

def isSafe(nums):
    boolIncreasing = all(i < j for i, j in zip(nums, nums[1:]))
    boolDecreasing = all(i > j for i, j in zip(nums, nums[1:]))
    return boolIncreasing or boolDecreasing

#open file and read it line-by-line to handle variable length rows
allNumsList = []
with open("inputDay2.csv", "r") as file:
    for line in file:
        rowList = list(map(int, line.strip().split()))  #turn row into list of ints
        # print(rowList)
        allNumsList.append(rowList)

safeCount = 0
for i in range(len(allNumsList)):
    isSafeNum = isSafe(allNumsList[i])
    # print("LIST TESTING:", allNumsList[i])
    unsafeDiff = 0
    for num in range(len(allNumsList[i]) - 1):
        diff = abs(allNumsList[i][num] - allNumsList[i][num + 1])
        # print(f"i[num]: {allNumsList[i][num]}, i[adj]: {allNumsList[i][num + 1]}, difference: {diff}")
        if 1 <= diff <= 3:
            # print("GOOD DIFF", diff)
            pass
        else:
            # print("DIFF IS WRONG", diff)
            unsafeDiff += 1

    if isSafeNum and unsafeDiff < 1:
        safeCount += 1
        # print("SAFE NUM", allNumsList[i], "\n")
    else:
        # print("UNSAFE NUM:", allNumsList[i], "\n")
        pass
print("SAFE COUNT PT 1:", safeCount, "\n")

####################################################
####################################################
# PT II



def safeWithoutnum(nums):
    if isSafe(nums) and all(1 <= abs(nums[i] - nums[i+1]) <= 3 for i in range(len(nums) - 1)):
        return True
    for i in range(len(nums)):
        modifiedListNums = nums[:i] + nums[i+1:]
        if isSafe(modifiedListNums) and all(1 <= abs(modifiedListNums[j] - modifiedListNums[j+1]) <= 3 for j in range(len(modifiedListNums) - 1)):
            return True
    return False

safeCount = 0  

for row in allNumsList:
    if safeWithoutnum(row):
        safeCount += 1

print("SAFE COUNT PT 2:", safeCount)




#THIS PART IS WRONG BY 1
# safeCount = 0

# for i in range(len(allNumsList)):
#     badLevelCount = 0
#     isSafeNum = isSafe(allNumsList[i])
#     print("\nLIST TESTING:", allNumsList[i])
#     unsafeDiff = 0
#     for num in range(len(allNumsList[i]) - 1):
#         diff = abs(allNumsList[i][num] - allNumsList[i][num + 1])
#         # print(f"i[num]: {allNumsList[i][num]}, i[adj]: {allNumsList[i][num + 1]}, difference: {diff}")
#         if 1 <= diff <= 3:
#             # print("good diff:", diff)
#             pass
#         else:
#             print("DIFF IS WRONG: ", allNumsList[i][num], "-", allNumsList[i][num + 1] , "=", diff)
#             # for first bad level, if popping it and then doing isSafe funct returns True
#             if badLevelCount == 0:
#                 print("OLD IS SAFE:", isSafeNum)
#                 copyallNumsList = copy.deepcopy(allNumsList[i])
#                 copyallNumsList.pop(num) 
#                 newIsSafe = isSafe(copyallNumsList)
#                 print(f"NEW IS SAFE WITHOUT NUM {allNumsList[i][num]}: {newIsSafe}")
#                 isSafeNum = newIsSafe
#                 print("OLD IS SAFE UPDATED:", isSafeNum)
#                 badLevelCount += 1
#             else:
#                 unsafeDiff += 1
            

#     if isSafeNum == True and unsafeDiff < 1:
#         safeCount += 1
#         # print("SAFE NUM", allNumsList[i], "\n")
#     else:
#         # print("UNSAFE NUM:", allNumsList[i], "\n")
#         pass

# print("\n\nSAFE COUNT PT 2:", safeCount)

