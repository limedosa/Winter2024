import pandas as pd 

df = pd.read_csv('inputDay1.csv', sep='   ', header=None)

col0 = df[0].tolist()
iters = df[0].tolist()
col1 = df[1].tolist()
listDif = []
count = 0 
print(f'length: {len(col0)}\n')
while count < (len(iters)):
    min0= min(col0)
    min1=min(col1)
    difference = abs(min1-min0)
    listDif.append(difference)
    # print(f"MIN0:{min0}, MIN1:{min1}, DIFFERENCE:{difference}")
    col0.remove(min0)
    col1.remove(min1)
    count +=1
print(f"PART I: {sum(listDif)}")


col0 = df[0].tolist()
col1 = df[1].tolist()
freq = 0
for i in col0:
    freq_i = col1.count(i)
    similarity = i * freq_i
    freq+=(similarity)
print(f"PART II: {freq}")