activities = {"scratched", "catch", "nap", "burying", "walk"}
dogs = {"Saber", "Ginger", "Nutmeg", "Pepper", "Bear"}

Pepper = activities - {"scratched", "nap", "walk"} # Pepper is either playing catch or burying a chew toy.
# Neither Ginger nor Saber nor Bear is on a walk.
Ginger = activities - {"walk"}
Saber = activities - {"walk"}
Bear = activities - {"walk"}

# One of the dogs named after a spice is getting its ears scratched.
Nutmeg = activities
Saber = Saber - {"scratched"}
Bear = Bear - {"scratched"}
# A dog not named for a spice is playing catch.
Pepper = Pepper - {"catch"}
Ginger = Ginger - {"catch"}
Nutmeg = Nutmeg - {"catch"}
# Bear is getting some exercise.
Bear = Bear - {"scratched", "nap"}

goodBoys = {"Pepper" : Pepper, "Ginger" : Ginger, "Saber" : Saber, "Bear" : Bear, "Nutmeg" : Nutmeg}

doing = set() # this contains the activities that have been figured out

while sum([len(goodBoys[dog]) for dog in goodBoys]) > len(goodBoys): # loop until each dog has exactly 1 activity currently being performed
    for dog in goodBoys:
        if len(goodBoys[dog]) == 1: # when a kid has exactly one favourite activity it will be add to favourite and continue loop
            doing.update(goodBoys[dog])
            continue
        goodBoys[dog] = goodBoys[dog] - doing


print(goodBoys)