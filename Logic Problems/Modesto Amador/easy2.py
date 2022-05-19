# The Good Life
# 5 neighborhood dogs are doing one of 5 activities
# Dogs = [Saber, Ginger, Nutmeg, Pepper, and Bear]
# Activities = [Ears scratching, playing catch, taking a nap, burying a chew toy, going for a walk]

# Statements
# Pepper is either playing catch or burying a chew toy.
# Neither Ginger nor Saber nor Bear is on a walk.
# One of the dogs named after a spice is getting its ears scratched.
# A dog not named for a spice is playing catch.
# Bear is getting some exercise.

#Code is not working right now
Saber = {"Catch", "Nap", "Bury"}
Ginger = {"Ears", "Catch", "Nap", "Bury"}
Nutmeg = {"Ears", "Walk"}
Pepper = {"Bury"}
Bear = {"Catch", "Bury"}
final = set()
Dogs = [Saber, Ginger, Nutmeg, Pepper, Bear]
i = 0
while len(Dogs) > 1:
    if(len(Dogs[i]) == 1):
        print(f"update dogs with {Dogs[i]}")
        final.update(Dogs[i])
        print(final)
        print(f"remove {Dogs[i]} from list")
        temp = "Dogs[i]"
        Dogs.remove(Dogs[i])
        for j in range(len(Dogs)):
            print("entered discard code")
            Dogs[j].discard("Bury")
        print(Dogs)
        i = 0
    else:
        i += 1
        
    


#final.update(Pepper)
# Elimate Bury from Bear. They are playing Catch
#Bear = Bear.difference(Pepper)
#final.update(Bear)
print(final)

print(f"Saber: {Saber}")
print(f"Bear: {Bear}")
print(f"Pepper: {Pepper}")
print(f"Nutmeg: {Nutmeg}")
print(f"Ginger: {Ginger}")

#Take Catch away from all other dogs
