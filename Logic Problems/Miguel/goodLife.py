
from functions import deduceTask

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

solution = deduceTask(goodBoys.copy())

print(solution)