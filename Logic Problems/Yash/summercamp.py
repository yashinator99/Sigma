

#cook, kayak, rock climb, and zip-line
abigail = [1, 1, 0, 1]
oliver = [1, 1, 0 , 0]
rosa = [0, 0, 1, 1]
blake = [1, 0, 0, 0]

all = [abigail, oliver, rosa, blake]
activities = 4
for k in range(activities):
    for i in range(4):
        count = 0
        idx = 0
        for j in range(4):
            if(all[i][j] == 1):
                count += 1
                idx = j
        if(count == 1):
            all[0][idx] = 0
            all[1][idx] = 0
            all[2][idx] = 0
            all[3][idx] = 0
            all[i][idx] = 1


#abigail = [0, 1, 1, 0]
#oliver = [0, 1, 0 , 0]
#rosa = [0, 0, 1, 1]
#blake = [1, 0, 0, 0]
print(all)