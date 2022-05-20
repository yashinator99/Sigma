

#Activities go from
#cook, kayak, rock climb, zip-line
abigail = [1, 1, 0, 1]
oliver  = [1, 1, 0, 0]
rosa    = [0, 0, 1, 1]
blake   = [1, 0, 0, 0]

# 1 means likes it
# 0 means doesnt like it

all = [abigail, oliver, rosa, blake]
activities = 4

#This program solution will provide
#abigail = [0, 0, 0, 1]
#oliver = [0, 1, 0 , 0]
#rosa = [0, 0, 1, 0]
#blake = [1, 0, 0, 0]

for k in range(activities):
    for people in range(len(all)):
        count = 0
        idx = 0
        for j in range(len(all[people])):
            if(all[people][j] == 1):
                count += 1
                idx = j
        if(count == 1):
            all[0][idx] = 0
            all[1][idx] = 0
            all[2][idx] = 0
            all[3][idx] = 0
            all[people][idx] = 1


print(f"Activities go from cook, kayak, rock climb, zip-line")
print(f"Abigail - {all[0]}")
print(f"Oliver  - {all[1]}")
print(f"Rosa    - {all[2]}")
print(f"Blake   - {all[3]}")