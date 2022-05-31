import collections
#people: Leisha, Benito, Delia, Charlotte, Weldon, and Zina

numberofpeople = 6
height = {}
#Weldon is taller than Delia but shorter than Zina.
height['Weldon'] = numberofpeople
height['Delia'] = height['Weldon'] - 3
height['Zina']  = height['Weldon'] + 3

#Leisha is taller than Benito but shorter than Delia and Weldon.
height['Leisha'] = height['Delia'] - 3
height['Benito'] = height['Leisha'] - 3

#Benito is not the shortest.

height['Charlotte'] = height['Benito'] - 3

od = collections.OrderedDict(sorted(height.items()))
print(od)