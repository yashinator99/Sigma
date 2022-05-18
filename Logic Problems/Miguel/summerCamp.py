# summer camp

activities = {"Cook", "Rock Climb", "Zip-line", "Kayak"}
kids = {"Abigail", "Oliver", "Rosa", "Blake"}

Abigail = activities - {"Rock Climb"} # Abigail’s favorite activity isn’t rock climbing.
Oliver = activities - {"Rock Climb", "Zip-line"} # Oliver is afraid of heights.
Rosa = activities - {"Cook", "Kayak"} # Rosa can’t do her favorite activity without a harness.
Blake = activities - {"Rock Climb", "Zip-line", "Kayak"} # Blake likes to keep his feet on the ground at all times.

campers = {"Abigail" : Abigail, "Oliver" : Oliver, "Rosa" : Rosa, "Blake" : Blake}
favourite = set() # this contains the activities that have been figured out

while sum([len(campers[kid]) for kid in campers]) > 4: # loop until each kid has exactly 1 favourite activity
    for kid in kids:
        if len(campers[kid]) == 1: # when a kid has exactly one favourite activity it will be add to favourite and continue loop
            favourite.update(campers[kid])
            continue
        campers[kid] = campers[kid] - favourite


print(campers)