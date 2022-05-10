import csv


with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))


# print(mpg[0].keys())
# print(mpg[0].values())
# print(len(mpg))
#
# for i in mpg:
#     print(i['trans'])
#
#
# print(mpg[0]['manufacturer'])

# d=0
# while (d!=len(mpg)):
#     print(mpg[d]['cty'])
#     d=d+1

# cylinders = set(d['cty'] for d in mpg)
#
# print(cylinders)
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)
CtyMpgByCyl = []

for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')
CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

CtyMpgByCyl1 = []
summpg1 = 0
summpg2 = 0
summpg3 = 0
summpg4 = 0
cyltypecount1 = 0
cyltypecount2 = 0
cyltypecount3 = 0
cyltypecount4 = 0
for d in mpg:
    if float(d['cyl']) == 4:
        summpg1 += float(d['cty'])
        cyltypecount1 += 1
        continue
    elif float(d['cyl']) == 5:
        summpg2 += float(d['cty'])
        cyltypecount2 += 1
        continue
    elif float(d['cyl']) == 8:
        summpg3 += float(d['cty'])
        cyltypecount3 += 1
        continue
    elif float(d['cyl']) == 6:
        summpg4 += float(d['cty'])
        cyltypecount4 += 1
        continue
CtyMpgByCyl1.append((4, summpg1 / cyltypecount1))
CtyMpgByCyl1.append((5, summpg2 / cyltypecount2))
CtyMpgByCyl1.append((8, summpg3 / cyltypecount3))
CtyMpgByCyl1.append((6, summpg4 / cyltypecount4))
CtyMpgByCyl1.sort(key=lambda x: x[0])
print(CtyMpgByCyl1)