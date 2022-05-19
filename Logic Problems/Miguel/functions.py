def deduceTask(individuals: dict) -> dict:
    deduced = set()
    while sum([len(individuals[tasks]) for tasks in individuals]) > len(individuals): # loop until each individual has exactly 1 task
        for tasks in individuals:
            if len(individuals[tasks]) == 1: # when an individual has exactly one task it will be added to deduced and continue loop
                deduced.update(individuals[tasks])
                continue
            individuals[tasks] = individuals[tasks] - deduced
    return individuals