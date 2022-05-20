

def generatePeople():
    abigail = [1, 1, 0, 1]
    oliver  = [1, 1, 0, 0]
    rosa    = [0, 0, 1, 1]
    blake   = [1, 0, 0, 0]
    return [abigail, oliver, rosa, blake]

def checkActivity(count, idx, all, person):
    for j in range(len(all[person])):
            if(all[person][j] == 1):
                count += 1
                idx = j
    return count, idx

def reset(idx, all, person):
    all[0][idx] = 0
    all[1][idx] = 0
    all[2][idx] = 0
    all[3][idx] = 0
    all[person][idx] = 1
    return all

def mainprocess():
    activities = 4
    all = generatePeople()
    for k in range(activities):
        for people in range(len(all)):
            count = 0
            idx = 0
            count, idx = checkActivity(count, idx, all, people)
            if(count == 1):
                all = reset(idx, all, people)
    return all

if __name__ == "__main__":
    all = mainprocess()
    print(f"Activities go from cook, kayak, rock climb, zip-line")
    print(f"Abigail - {all[0]}")
    print(f"Oliver  - {all[1]}")
    print(f"Rosa    - {all[2]}")
    print(f"Blake   - {all[3]}")