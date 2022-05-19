from functions import deduceTask

dads = set()
students = set()

# Stephanie went to the senior prom with Michael’s son.
dads.update({"Michael"})
students.update({"Stephanie"})
# Elias and James played on the school’s baseball team. One of them is Alberto’s son.
students.update({"Elias", "James"})
dads.update({"Alberto", "Ken"})
# Michael and Elias are not related.
parents = {dad : students for dad in dads}
parents["Michael"] = parents["Michael"] - {"Elias"}

parents["Michael"] = parents["Michael"] - {"Stephanie"} # Stephanie went to the senior prom with Michael’s son.
parents["Alberto"] = parents["Alberto"] - {"Stephanie"} # Elias and James played on the school’s baseball team. One of them is Alberto’s son.

solution = deduceTask(parents.copy())

print(solution)