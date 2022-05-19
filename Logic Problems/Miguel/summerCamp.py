# summer camp

from functions import deduceTask

activities = {"Cook", "Rock Climb", "Zip-line", "Kayak"}
kids = {"Abigail", "Oliver", "Rosa", "Blake"}

Abigail = activities - {"Rock Climb"} # Abigail’s favorite activity isn’t rock climbing.
Oliver = activities - {"Rock Climb", "Zip-line"} # Oliver is afraid of heights.
Rosa = activities - {"Cook", "Kayak"} # Rosa can’t do her favorite activity without a harness.
Blake = activities - {"Rock Climb", "Zip-line", "Kayak"} # Blake likes to keep his feet on the ground at all times.

campers = {"Abigail" : Abigail, "Oliver" : Oliver, "Rosa" : Rosa, "Blake" : Blake}

solution = deduceTask(campers.copy())

print(solution)