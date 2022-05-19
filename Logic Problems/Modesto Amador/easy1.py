# Summer Camp
# There are 4 campers
# There are 4 activities
# Each camper has a different favorite activity


# Messages
# A - Abigail's doesnt like rock climbing
# B - Oliver is scared of heights
# C - Rosa cant do her favorite activity without a harness
# D - Blake likes to keep his feet on the ground at all times

# Likes = True
# Dislikes = False

# Can you figute out who likes what?

#Activites = [cook, kayak, rock climb, and zip-line]

# Abigail
test_1 = [True, True, False, True]
# Oliver
test_2 = [True, True, False, False]
# Rosa
test_3 = [False, False, True, True]
# Blake
test_4 = [True, False, False, False]

# If blake only likes one thing, that is our base and we know he likes cooking
# Oliver likes cooking and kayaking, since cooking is blakes favorite, oliver's favorite is kayaking
# Abigail likes everything but rock climbing, her favorite must be zip-lining
# This leaves Rosa with her favorite being rock climbing
# Answer
# test_1 = [False, False, False, True]
# test_2 = [False, True, False, False]
# test_3 = [False, False, True, False]
# test_4 = [True, False, False, False]

test_cases = [test_1, test_2, test_3, test_4]

for i in range(len(test_cases)):
    for j in range(len(test_cases)):
        for k in range(len(test_cases)):
            x = test_cases[j].count(True)
            if(x == 1):
                #print(j)
                if(test_cases[j][k] == True):
                    #print("This is the only true statement")
                    if(j == 0):
                        #print("changed index 0")
                        test_cases[0][k] = True
                        test_cases[1][k] = False
                        test_cases[2][k] = False
                        test_cases[3][k] = False
                    elif(j == 1):
                        #print("changed index 1")
                        test_cases[0][k] = False
                        test_cases[1][k] = True
                        test_cases[2][k] = False
                        test_cases[3][k] = False
                    elif(j == 2):
                        #print("changed index 2")
                        test_cases[0][k] = False
                        test_cases[1][k] = False
                        test_cases[2][k] = True
                        test_cases[3][k] = False
                    elif(j == 3):
                        #print("changed index 3")
                        test_cases[0][k] = False
                        test_cases[1][k] = False
                        test_cases[2][k] = False
                        test_cases[3][k] = True
print(f"Activites: [cook, kayak, rock climb, and zip-line]")
print(f"Abigail's Favorite Activity:\n{test_1}\nOliver's Favorite Activity:\n{test_2}\nRosa's Favorite Activity:\n{test_3}\nBlake's Favorite Activity:\n{test_4}")