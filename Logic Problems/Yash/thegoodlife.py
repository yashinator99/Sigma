#getting its ears scratched, playing catch, taking a nap, burying a chew toy, and going for a walk
saber = [0, 0, 1, 0, 1]
ginger = [1, 0, 0 , 0, 0]
nutmeg = [0, 0, 0, 0, 1]
pepper  = [0, 1, 0, 1, 0]
bear = [0, 1, 0, 0, 0]
all = [saber, ginger, nutmeg, pepper, bear]
activities = 5
for k in range(activities):
    for i in range(5):
        count = 0
        idx = 0
        for j in range(5):
            if(all[i][j] == 1):
                count += 1
                idx = j
        if(count == 1):
            all[0][idx] = 0
            all[1][idx] = 0
            all[2][idx] = 0
            all[3][idx] = 0
            all[4][idx] = 0
            all[i][idx] = 1
print(all)
