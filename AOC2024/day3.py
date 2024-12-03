import pandas as pd 
import re
import math
# df = pd.read_html("https://uk-air.defra.gov.uk/data/DAQI-regional-data?regionIds%5B%5D=999&aggRegionId%5B%5D=999&datePreset=6&startDay=01&startMonth=01&startYear=2022&endDay=01&endMonth=01&endYear=2023&queryId=&action=step2&go=Next+")[0]

multList = []

with open("day3.txt", "r") as f:
    for line in f:
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        multList.extend(matches)
            
# print(multList[:100])
# print(len(multList))
final = 0
for strMult in range(len(multList)):
    nums = multList[strMult].split(",")
    multipied = 1
    for num in nums:
        # print("Num:", num, "Nums:",nums)
        digits = ''.join(filter(lambda char: char.isdigit(), num))
        # mult.append(int(digits))
        # print(digits)
        multipied *= int(digits)
    final += multipied

print("FINAL PT I:", final) 