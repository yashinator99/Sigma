#getting its ears scratched, playing catch, taking a nap, burying a chew toy, and going for a walk

#Have to hard code the message for each dog but gets the answer

# Pepper is either playing catch or burying a chew toy.
# Neither Ginger nor Saber nor Bear is on a walk.
# One of the dogs named after a spice is getting its ears scratched.
# A dog not named for a spice is playing catch.
# Bear is getting some exercise.
#
# Which gives us this
saber = [0, 0, 1, 0, 1]
ginger = [1, 1, 0 , 0, 0]
nutmeg = [0, 1, 0, 0, 1]
pepper  = [0, 1, 0, 1, 0]
bear = [0, 1, 0, 0, 0]
all = [saber, ginger, nutmeg, pepper, bear]
activities = 5
for k in range(activities):
    for dogs in range(len(all)):
        count = 0
        idx = 0
        for j in range(len(all[dogs])):
            if(all[dogs][j] == 1):
                count += 1
                idx = j
        if(count == 1):
            all[0][idx] = 0
            all[1][idx] = 0
            all[2][idx] = 0
            all[3][idx] = 0
            all[4][idx] = 0
            all[dogs][idx] = 1

print(f"Activities for the dog are getting its ears scratched, playing catch, taking a nap, burying a chew toy, going for a walk")
print(f"Saber  - {all[0]}")
print(f"Ginger - {all[1]}")
print(f"Nutmeg - {all[2]}")
print(f"Pepper - {all[3]}")
print(f"Bear   - {all[4]}")